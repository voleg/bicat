#coding: utf-8
from django.db import models
from managers import ItemManager
from parse import parse_item_to_dict, get_marc_string, get_marc_field, item_timestamp_format, ListToStr
from fields import TagSubtagField, JSONField, MarcItemField, MarcItemAuthorField

class MarcField(models.TextField):
    pass

# todo реализовать связи через content-type framework

class Inv(models.Model):
    """
    Модель таблицы экземпляров хранения,состоящих на учете

    """
    inv_id = models.IntegerField('идентификатор экземпляра хранения', primary_key=True, db_column=u'INV_ID')
    doc_id = models.IntegerField('ID Документа', db_column=u'DOC_ID')
    t990t = models.CharField('N записи в КСУ для И/У и  Б/У', max_length=255, db_column=u'T990t', blank=True)
    t090h = models.CharField('формат', max_length=255, db_column=u'T090h', blank=True)
    t090e = models.CharField('инвентарный номер', max_length=255, db_column=u'T090e', blank=True)
    t090f = models.CharField('сигла хранения', max_length=255, db_column=u'T090f', blank=True)
    t090w = models.CharField('номер фонда', max_length=255, db_column=u'T090w', blank=True)
    t876c = models.CharField('цена', max_length=255, db_column=u'T876c', blank=True)
    t876p = models.CharField('штрих-код', max_length=255, db_column=u'T876p', blank=True)
    t020d = models.CharField('денежная единица', max_length=255, db_column=u'T020d', blank=True)
    t020e = models.CharField('валютная цена', max_length=255, db_column=u'T020e', blank=True)
    t990n = models.CharField('номер УК(Б/У)', max_length=255, db_column=u'T990n', blank=True)
    cnt = models.IntegerField('количество экземпляров', null=True, db_column=u'CNT', blank=True)
    regdate = models.FloatField('дата и время ввода информации', null=True, db_column=u'REGDATE', blank=True)
    invmode = models.CharField('признак учета', max_length=1, db_column=u'INVMODE', blank=True)
    custom1 = models.CharField(max_length=255, db_column=u'CUSTOM1', blank=True)
    custom2 = models.CharField(max_length=255, db_column=u'CUSTOM2', blank=True)
    custom3 = models.CharField(max_length=255, db_column=u'CUSTOM3', blank=True)
    custom4 = models.CharField(max_length=255, db_column=u'CUSTOM4', blank=True)
    custom5 = models.CharField(max_length=255, db_column=u'CUSTOM5', blank=True)
    def __unicode__(self):
        return 'doc: %s invenatry code: %s' % (self.doc_id, self.t090e)

    class Meta:
        db_table = u'INV'
        abstract = True
        verbose_name = u'экземпляр хранения'
        verbose_name_plural = u'экземпляры хранения'


class Invoff(models.Model):
    """
    Модель журнала списания инвентарных номеров
    """
    inv_id = models.IntegerField('идентификатор экземпляра хранения', primary_key=True, db_column=u'INV_ID')
    doc_id = models.IntegerField('ID Документа', db_column=u'DOC_ID')
    t990t = models.CharField('N записи в КСУ для И/У', max_length=255, db_column=u'T990t', blank=True)
    t090h = models.CharField('формат', max_length=255, db_column=u'T090h', blank=True)
    t090e = models.CharField('инвентарный номер', max_length=255, db_column=u'T090e', blank=True)
    t090f = models.CharField('сигла хранения', max_length=255, db_column=u'T090f', blank=True)
    t090w = models.CharField('номер фонда', max_length=255, db_column=u'T090w', blank=True)
    t876c = models.CharField('цена', max_length=255, db_column=u'T876c', blank=True)
    t876p = models.CharField('штрих-код', max_length=255, db_column=u'T876p', blank=True)
    t020d = models.CharField('денежная единица', max_length=255, db_column=u'T020d', blank=True)
    t020e = models.CharField('валютная цена', max_length=255, db_column=u'T020e', blank=True)
    t990n = models.CharField('номер УК(Б/У)', max_length=255, db_column=u'T990n', blank=True)
    cnt = models.IntegerField('количество экземпляров(И/У=1,Б/У=Х)', null=True, db_column=u'CNT', blank=True)
    offdate = models.FloatField('дата и время списания', null=True, db_column=u'OFFDATE', blank=True)
    invmode = models.CharField('признак учета(И/У или И/У)', max_length=1, db_column=u'INVMODE', blank=True)
    notes = models.CharField('причина списания', max_length=255, db_column=u'NOTES', blank=True)
    wroffact = models.CharField('номер акта списания', max_length=255, db_column=u'WROFFACT', blank=True)
    custom1 = models.CharField(max_length=255, db_column=u'CUSTOM1', blank=True)
    custom2 = models.CharField(max_length=255, db_column=u'CUSTOM2', blank=True)
    custom3 = models.CharField(max_length=255, db_column=u'CUSTOM3', blank=True)
    custom4 = models.CharField(max_length=255, db_column=u'CUSTOM4', blank=True)
    custom5 = models.CharField(max_length=255, db_column=u'CUSTOM5', blank=True)
    def __unicode__(self):
        return 'doc: %s invenatry code: %s' % (self.doc_id, self.t090e)

    class Meta:
        db_table = u'INVOFF'
        abstract = True
        verbose_name = u'журнал списания'
        verbose_name_plural = u'Списанные инвентарные номера'


class Tag(models.Model):
    tag = models.CharField("номер поля (марковкском формате)", max_length=3, primary_key=True, db_column='TAG')
    subtag = models.CharField("буква подполя", max_length=1, db_column='SUBTAG', blank=True)
    flags = models.IntegerField("Флаги", null=True, db_column='FLAGS', blank=True)
    separator = models.CharField("Разделитель", max_length=1, db_column='SEPARATOR', blank=True)
    caption = models.CharField("Наименование", max_length=40, db_column='CAPTION', blank=True)

    def __unicode__(self):
        return " ".join([self.tag, self.subtag, self.caption])
    class Meta:
#        unique_together = (("tag", "subtag"),)
        db_table = u'TAG'
        abstract = True
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'

class Doc(models.Model):
    """
    Список Документов
    Table with docs items. The Item Field in the DB hard coded in MARC format see https://bitbucket.org/voleg/bicat/wiki/Поле%20ITEM
    """
    doc_id = models.IntegerField("№ Документа", primary_key=True, db_column='DOC_ID')
    rectype = models.CharField("тип записи", max_length=1, db_column='RECTYPE', blank=True)
    biblevel = models.CharField("библиотечный уровень", max_length=1, db_column='BIBLEVEL', blank=True)
    item = models.TextField("документ в макроподобном формате", db_column='ITEM', blank=True)
#    ITEM = MarcItemField("документ в макроподобном формате", db_column='ITEM', blank=True)

    objects = ItemManager()

    item_name = lambda self, tag=None, subtag=None: get_marc_field(self.item, tag=tag, subtag=subtag)
    # ... Тут дальше крамешный ад, что делать, с которым пока непонял, так, что лепим пока так

    def item_author(self):
        """
        извлекаем Авторов из Item
        """
        rel = None
        author = get_marc_field(self.item, tag='100', subtag='a')
        other_authors = get_marc_field(self.item, tag='700', subtag='a')
        if author == "" or other_authors == "": splitter = u''
        else: splitter = u', '
        return splitter.join([author,other_authors])

    @property
    def item_faculty(self):
        """ Кафедра """
        return get_marc_field(self.item, tag='903', subtag='d')

    @property
    def item_source(self):
        """ Источник поступления"""
        return get_marc_field(self.item, tag='901', subtag='a')
    @property
    def item_speciality(self):
        """ Специальность (направление) """
        return get_marc_field(self.item, tag='903', subtag='a')
    @property
    def item_type_work_program(self):
        """ Вид (контрольная, лабораторная, рабочая программа) """
        return get_marc_field(self.item, tag='903', subtag='f')

    @property
    def bibliographic_level(self):
        r"""Returns label for bibliographic level code from self.data"""
        blvls = {
            'a': 'Часть Монографии',
            'b': 'Часть Серии',
            'c': 'Колекция',
            'd': 'Подъединица',
            'i': 'Ресурс Интеграции',
            'm': 'Монография',
            's': 'Серия'
        }
        return blvls[self.biblevel]

    @property
    def item_place_and_date_of_publication(self):
        """
        773
            d	Место и дата издания:
                2012.-№12
            g	Прочая информация:
                С.61-83
            t	Название источника:
                Вопросы экономики
        """
        return get_marc_field(self.item, tag='773', subtag='d')

    @property
    def item_other_information(self):
        return get_marc_field(self.item, tag='773', subtag='g')

    @property
    def item_source_name(self):
        return get_marc_field(self.item, tag='773', subtag='t')

    @property
    def item_author_main(self):
        return get_marc_field(self.item, tag='100', subtag='a')

    @property
    def item_authors_other(self):
        return get_marc_field(self.item, tag='700', subtag='a')

    @property
    def item_last_change_timestamp(self):
        """извлекаем дату последней правки из Item"""
        timestamp = get_marc_field(self.item, tag='005', subtag='0')
        return item_timestamp_format(timestamp)

    @property
    def item_entrence_date(self):
        """Дата поступления"""
        entrance_date = get_marc_field(self.item, tag='990', subtag='f')
        return entrance_date

    @property
    def item_series(self):
        """Серия"""
        series = get_marc_field(self.item, tag='440')
        return series

    @property
    def item_ISBN(self):
        """ISBN """
        return get_marc_field(self.item, tag='020', subtag='a')

    @property
    def item_cost(self):
        """Цена"""
        return get_marc_field(self.item, tag='020', subtag='c')

    @property
    def item_bibliography(self):
        return get_marc_field(self.item, tag='504', subtag='a')

    @property
    def item_pages(self):
        """Объём издания"""
        return get_marc_field(self.item, tag='300', subtag='a')

    @property
    def item_illustrations(self):
        """ Илл./тип воспроизв. """
        return get_marc_field(self.item, tag='300', subtag='b')

    @property
    def item_format(self):
        """ Формат """
        return get_marc_field(self.item, tag='300', subtag='c')
    @property
    def item_cover(self):
        """
        300
            d	Вид переплета:
                В пер.
            a	Объем:
                1028 с.
            e	Сопров.мат:
                ил.
        """
        return get_marc_field(self.item, tag='300', subtag='d')

    @property
    def item_covering_matireals(self):
        return get_marc_field(self.item, tag='300', subtag='e')

    @property
    def item_shelving_index(self):
        """
        090
            a	Полочн.индекс:
                65.9(2Рос)-56
            c	Кат.индекс:
                65.9(2Рос)-56я73
            x	Авторский знак:
                Ш 26
            w	Номер фонда:
                ч.з
            e	Инвентарный номер:
                13365
                ...
        """
        return get_marc_field(self.item, tag='090', subtag='a')

    @property
    def item_cat_index(self):
        return get_marc_field(self.item, tag='090', subtag='c')

    @property
    def item_author_lable(self):
        return get_marc_field(self.item, tag='090', subtag='x')

    @property
    def item_invent_code(self):
        return get_marc_field(self.item, tag='090', subtag='e')


    @property
    @ListToStr
    def item_title(self):
        """ Заглавие - основное заглавие, например "Инвестиции" """
        return get_marc_field(self.item, tag='245', subtag='a')

    @property
    def item_next_title(self):
        """ Заглавие - Продолж.заглавия, например "Заглавие" """
        return get_marc_field(self.item, tag='245', subtag='b')

    @property
    def item_responsibility(self):
        """Заглавие - Ответственность, например "Пер. с англ." """
        return get_marc_field(self.item, tag='245', subtag='c')

    @property
    def item_title_date_of_works(self):
        """Заглавие - Даты произведения """
        return get_marc_field(self.item, tag='245', subtag='f')

    @property
    def item_title_media(self):
        """Заглавие - Носитель """
        return get_marc_field(self.item, tag='245', subtag='h')

    @property
    def item_title_part_number(self):
        """Заглавие - Номер части """
        return get_marc_field(self.item, tag='245', subtag='n')

    @property
    def item_title_parallel_title(self):
        """Заглавие - Паралельное заглавие """
        return get_marc_field(self.item, tag='245', subtag='o')

    @property
    def item_title_part_name(self):
        """Заглавие - Название части """
        return get_marc_field(self.item, tag='245', subtag='p')

    @property
    def item_title_version(self):
        """Заглавие - Версия """
        return get_marc_field(self.item, tag='245', subtag='s')

    def item_publish(self):
        """
        260
            b	Издательство:
                ИНФРА-М
            c	Дата издания:
                2012
            a	Место издания:
                М.
                ...
        """
        return get_marc_field(self.item, tag='260')

    @property
    def item_place(self):
        return get_marc_field(self.item, tag='260', subtag='a')

    @property
    def item_publisher(self):
        return get_marc_field(self.item, tag='260', subtag='b')

    @property
    def item_publication_year(self):
        return get_marc_field(self.item, tag='260', subtag='c')

    @property
    def item_remarks(self):
        return get_marc_field(self.item, tag='500', subtag='a')

    def item_tags(self):
        """
        653
            a	Ключевые слова:
                Новая Российская энциклопедия;Энциклопедия
        """
        return get_marc_field(self.item, tag='653', subtag='a')
    # Todo Теги должны извлекаться списком

    @property
    def item_dict_full(self):
        return "".join([str(self.doc_id),": ",get_marc_string(parse_item_to_dict(self.item))])

    @property
    def item_dict(self):
        return ''.join([self.item_dict_full[:600], ' ...'])

    @property
    def item_json(self):
        return parse_item_to_dict(self.item)

    def __unicode__(self):
#        return " ".join([str(self.doc_id), self.item_author(), self.item_title()[:80]])
        return unicode(self.doc_id)

    @models.permalink
    def get_absolute_url(self):
        name = '%s_doc-path' % (self._meta.app_label)
        return name, [self.doc_id]

    class Meta:
        db_table = u'DOC'
        abstract = True
        verbose_name = u'Документ'
        verbose_name_plural = u'Документы'

class Idx100Ax(models.Model):
    idx_id = models.IntegerField(primary_key=True, null=False, db_column='IDX_ID', blank=True)
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID')
    class Meta:
        db_table = u'IDX100aX'
        abstract = True

class Idx100A(models.Model):
    """ Словарь Авторов """
    idx_id = models.IntegerField(db_column='IDX_ID')
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM')
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True)
    class Meta:
        db_table = u'IDX100a'
        abstract = True

class Idx653Ax(models.Model):
    idx_id = models.IntegerField(primary_key=True, db_column=u'IDX_ID')
    doc_id = models.IntegerField(db_column=u'DOC_ID')

    class Meta:
        db_table = u'IDX653aX'
        abstract = True

class Idx653A(models.Model):
    """ Словарь Тегов """
    idx_id = models.IntegerField(db_column='IDX_ID')
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM')
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True)
    class Meta:
        db_table = u'IDX653a'
        abstract = True

class Idx245Ax(models.Model):
    idx_id = models.IntegerField(primary_key=True, null=False, db_column='IDX_ID', blank=True)
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID')

    class Meta:
        db_table = u'IDX245aX'
        abstract = True

class Idx245A(models.Model):
    """ Словарь Заглавий публикаций """
    idx_id = models.IntegerField(db_column='IDX_ID',)
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM')
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True)
    class Meta:
        db_table = u'IDX245a'
        abstract = True