#coding: utf-8
from django.db import models
from django.contrib.contenttypes.models import ContentType
from managers import ItemManager
from parse import parse_item_to_dict, get_marc_string, get_marc_field
from fields import MarcItemField, ItemField

class DocInv(models.Model):
    """
    Dirty workaround model to tie Doc and Inv Legacy Models, i do not want to alter
    Represents a through model in many-to-many relation
    """
    # id = models.PositiveIntegerField(primary_key=True, db_column=u'INV_ID')
    docinv_id = models.ForeignKey("Inv", primary_key=True, db_column=u'INV_ID')
    docdoc_id = models.ForeignKey("Doc", db_column=u'DOC_ID')

    class Meta:
        auto_created =True
        abstract = True
        db_table = u'INV'



class DocInvOff(models.Model):
    """
    Dirty workaround model to tie Doc and Inv Legacy Models, i do not want to alter
    Represents a through model in many-to-many relation
    """
    # id = models.PositiveIntegerField(primary_key=True, db_column=u'INV_ID')
    docinvoff_id = models.ForeignKey("Invoff", primary_key=True, db_column=u'INV_ID')
    docdoc_id = models.ForeignKey("Doc", db_column=u'DOC_ID')

    class Meta:
        auto_created = True
        db_table = u'INVOFF'
        abstract = True


class Inv(models.Model):
    """
    Модель таблицы экземпляров хранения,состоящих на учете
    """
    inv_id = models.PositiveIntegerField('идентификатор экземпляра хранения', primary_key=True, db_column=u'INV_ID')
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

    sigla = models.ForeignKey('Siglas', to_field='shortname', db_column=u'T090f')

    def __unicode__(self):
        return u'%s / %s: %s шт' % (unicode(self.t090e), unicode(self.t090f), unicode(self.cnt))

    class Meta:
        db_table = u'INV'
        abstract = True
        verbose_name = u'экземпляр хранения'
        verbose_name_plural = u'экземпляры хранения'


class Invoff(models.Model):
    """
    Модель журнала списания инвентарных номеров
    """
    inv_id = models.PositiveIntegerField('идентификатор экземпляра хранения', primary_key=True, db_column=u'INV_ID')
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

    sigla = models.ForeignKey('Siglas', to_field='shortname', db_column=u'T090f')

    def __unicode__(self):
        return u'%s / %s: %s шт, списан: %s %s' % (unicode(self.t090e), unicode(self.t090f), unicode(self.cnt), unicode(self.offdate), unicode(self.notes))

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
        verbose_name_plural = u'плохие Теги'

class Tags(models.Model):
    """
    a Cloned model from legacy MSSQL DB, where tag and subtag fields are index together
    the new model is the same structure and actually a data + id index field
    the reason is dj1.4 it seems cant index together 2 fields(tag+subtag)
    """
    tag = models.CharField("номер поля", max_length=3, blank=True, null=True)
    subtag = models.CharField("буква подполя", max_length=1, blank=True, null=True)
    flags = models.IntegerField("Флаги", null=True, blank=True)
    separator = models.CharField("Разделитель", max_length=1, blank=True, null=True)
    caption = models.CharField("Наименование", max_length=40, blank=True, null=True)

    def __unicode__(self):
        return " ".join([self.tag, self.subtag, self.caption])

    class Meta:
        unique_together = (("tag", "subtag"),)
        verbose_name = u'Тег'
        verbose_name_plural = u'Основные Теги'


class Doc(models.Model):
    """
    Список Документов Реализация на Model-instance методах (fast)
    Table with docs items. The Item Field in the DB hard coded in MARC
    format see https://bitbucket.org/voleg/bicat/wiki/Поле%20ITEM
    """
    blvls = {
        'a': 'Часть Монографии',
        'b': 'Часть Серии',
        'c': 'Колекция',
        'd': 'Подъединица',
        'i': 'Ресурс Интеграции',
        'm': 'Монография',
        's': 'Серия'
    }

    doc_id = models.PositiveIntegerField("№ Документа", primary_key=True, db_column='DOC_ID')
    rectype = models.CharField("тип записи", max_length=1, db_column='RECTYPE', blank=True)
    biblevel = models.CharField("библиотечный уровень", max_length=1, db_column='BIBLEVEL', blank=True, choices=((x, y) for x,y in blvls.items()))
    item_raw = models.TextField("документ в макроподобном формате", db_column='ITEM', blank=True)
    item = ItemField("документ в макроподобном формате", db_column='ITEM', blank=True)

    # Using inventory information from legacy DB
    inventory_number = models.ManyToManyField('Inv', through='DocInv', verbose_name='Экземпляры хранения')
    inventory_offs = models.ManyToManyField('Invoff', through='DocInvOff', verbose_name='Списание')

    # Using dictionaries produced by MarcSQL from legacy DB
    marc_indexed_authors = models.ManyToManyField('Idx100A', through='Idx100Ax', verbose_name='Словарь Авторов')
    marc_indexed_tags = models.ManyToManyField('Idx653A', through='Idx653Ax', verbose_name='Словарь Тегов')
    marc_indexed_titles = models.ManyToManyField('Idx245A', through='Idx245Ax', verbose_name='Словарь Заглавий')
    marc_indexed_years = models.ManyToManyField('Idx260C', through='Idx260Cx', verbose_name='Даты публикаций')

    objects = ItemManager()

    @property
    def bibliographic_level(self):
        r"""Returns label for bibliographic level code from self.data"""
        return self.blvls[self.biblevel]

    def get_ct(self):
        return ContentType.objects.get_for_model(self)

    def __unicode__(self):
        return unicode(" ".join([str(self.doc_id), self.item_author(), unicode(self.item_title()[:80])]))

    @models.permalink
    def get_absolute_url(self):
        name = '%s_doc-path' % (self._meta.app_label)
        return name, [self.doc_id]

    class Meta:
        db_table = u'DOC'
        abstract = True
        verbose_name = u'Документ'
        verbose_name_plural = u'Документы'

class Doc_0(models.Model):
    """
    Список Документов Реализация на Model-instance методах (fast)
    Table with docs items. The Item Field in the DB hard coded in MARC
    format see https://bitbucket.org/voleg/bicat/wiki/Поле%20ITEM

    """
    doc_id = models.IntegerField("№ Документа", primary_key=True, db_column='DOC_ID')
    rectype = models.CharField("тип записи", max_length=1, db_column='RECTYPE', blank=True)
    biblevel = models.CharField("библиотечный уровень", max_length=1, db_column='BIBLEVEL', blank=True)
    item_raw = models.TextField("документ в макроподобном формате", db_column='ITEM', blank=True)
    item = ItemField("документ в макроподобном формате", db_column='ITEM', blank=True)

#    test = VirtualField(tag='100', subtag='a')

    objects = ItemManager()

    # ... Тут дальше крамешный ад, что делать, с которым пока непонял, так, что лепим пока так

#    def item_author(self):
#        """
#        извлекаем Авторов из Item
#        """
#        author = get_marc_field(self.item, tag='100', subtag='a')
#        other_authors = get_marc_field(self.item, tag='700', subtag='a')
#        if author == "" or other_authors == "": splitter = u''
#        else: splitter = u', '
#        return splitter.join([author, other_authors])

#    @property
#    def item_faculty(self):
#        """ Кафедра """
#        return get_marc_field(self.item, tag='903', subtag='d')

#    @property
#    def item_source(self):
#        """ Источник поступления"""
#        return get_marc_field(self.item, tag='901', subtag='a')

#    @property
#    def item_speciality(self):
#        """ Специальность (направление) """
#        return get_marc_field(self.item, tag='903', subtag='a')

#    @property
#    def item_type_work_program(self):
#        """ Вид (контрольная, лабораторная, рабочая программа) """
#        return get_marc_field(self.item, tag='903', subtag='f')

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

#    @property
#    def item_place_and_date_of_publication(self):
#        """
#        773
#            d	Место и дата издания:
#                2012.-№12
#            g	Прочая информация:
#                С.61-83
#            t	Название источника:
#                Вопросы экономики
#        """
#        return get_marc_field(self.item, tag='773', subtag='d')

#    @property
#    def item_other_information(self):
#        return get_marc_field(self.item, tag='773', subtag='g')

#    @property
#    def item_source_name(self):
#        return get_marc_field(self.item, tag='773', subtag='t')

#    @property
#    def item_author_main(self):
#        return get_marc_field(self.item, tag='100', subtag='a')

#    @property
#    def item_authors_other(self):
#        return get_marc_field(self.item, tag='700', subtag='a')

#    @property
#    def item_last_change_timestamp(self):
#        """извлекаем дату последней правки из Item"""
#        timestamp = get_marc_field(self.item, tag='005', subtag='0')
#        return item_timestamp_format(timestamp)
#
#    @property
#    def item_entrence_date(self):
#        """Дата поступления"""
#        entrance_date = get_marc_field(self.item, tag='990', subtag='f')
#        return entrance_date

#    @property
#    def item_series(self):
#        """Серия"""
#        series = get_marc_field(self.item, tag='440')
#        return series

#    @property
#    def item_ISBN(self):
#        """ISBN """
#        return get_marc_field(self.item, tag='020', subtag='a')

#    @property
#    def item_cost(self):
#        """Цена"""
#        return get_marc_field(self.item, tag='020', subtag='c')

#    @property
#    def item_bibliography(self):
#        return get_marc_field(self.item, tag='504', subtag='a')

#    @property
#    def item_pages(self):
#        """Объём издания"""
#        return get_marc_field(self.item, tag='300', subtag='a')
#
#    @property
#    def item_illustrations(self):
#        """ Илл./тип воспроизв. """
#        return get_marc_field(self.item, tag='300', subtag='b')

#    @property
#    def item_format(self):
#        """ Формат """
#        return get_marc_field(self.item, tag='300', subtag='c')

#    @property
#    def item_cover(self):
#        """
#        300
#            d	Вид переплета:
#                В пер.
#            a	Объем:
#                1028 с.
#            e	Сопров.мат:
#                ил.
#        """
#        return get_marc_field(self.item, tag='300', subtag='d')

#    @property
#    def item_covering_matireals(self):
#        return get_marc_field(self.item, tag='300', subtag='e')

#    @property
#    def item_shelving_index(self):
#        """
#        090
#            a	Полочн.индекс:
#                65.9(2Рос)-56
#            c	Кат.индекс:
#                65.9(2Рос)-56я73
#            x	Авторский знак:
#                Ш 26
#            w	Номер фонда:
#                ч.з
#            e	Инвентарный номер:
#                13365
#                ...
#        """
#        return get_marc_field(self.item, tag='090', subtag='a')

#    @property
#    def item_cat_index(self):
#        return get_marc_field(self.item, tag='090', subtag='c')

#    @property
#    def item_author_lable(self):
#        return get_marc_field(self.item, tag='090', subtag='x')

#    @property
#    def item_invent_code(self):
#        return get_marc_field(self.item, tag='090', subtag='e')


#    @property
#    @ListToStr
#    def item_title(self):
#        """ Заглавие - основное заглавие, например "Инвестиции" """
#        return get_marc_field(self.item, tag='245', subtag='a')

#    @property
#    def item_next_title(self):
#        """ Заглавие - Продолж.заглавия, например "Заглавие" """
#        return get_marc_field(self.item, tag='245', subtag='b')

#    @property
#    def item_responsibility(self):
#        """Заглавие - Ответственность, например "Пер. с англ." """
#        return get_marc_field(self.item, tag='245', subtag='c')

#    @property
#    def item_title_date_of_works(self):
#        """Заглавие - Даты произведения """
#        return get_marc_field(self.item, tag='245', subtag='f')

#    @property
#    def item_title_media(self):
#        """Заглавие - Носитель """
#        return get_marc_field(self.item, tag='245', subtag='h')

#    @property
#    def item_title_part_number(self):
#        """Заглавие - Номер части """
#        return get_marc_field(self.item, tag='245', subtag='n')

#    @property
#    def item_title_parallel_title(self):
#        """Заглавие - Паралельное заглавие """
#        return get_marc_field(self.item, tag='245', subtag='o')

#    @property
#    def item_title_part_name(self):
#        """Заглавие - Название части """
#        return get_marc_field(self.item, tag='245', subtag='p')

#    @property
#    def item_title_version(self):
#        """Заглавие - Версия """
#        return get_marc_field(self.item, tag='245', subtag='s')
#
#    def item_publish(self):
#        """
#        260
#            b	Издательство:
#                ИНФРА-М
#            c	Дата издания:
#                2012
#            a	Место издания:
#                М.
#                ...
#        """
#        return get_marc_field(self.item, tag='260')

#    @property
#    def item_place(self):
#        return get_marc_field(self.item, tag='260', subtag='a')

#    @property
#    def item_publisher(self):
#        return get_marc_field(self.item, tag='260', subtag='b')

#    @property
#    def item_publication_year(self):
#        return get_marc_field(self.item, tag='260', subtag='c')

#    @property
#    def item_remarks(self):
#        return get_marc_field(self.item, tag='500', subtag='a')

#    def item_tags(self):
#        """
#        653
#            a	Ключевые слова:
#                Новая Российская энциклопедия;Энциклопедия
#        """
#        return get_marc_field(self.item, tag='653', subtag='a')

    @property
    def item_dict_full(self):
        return "".join([str(self.doc_id), ": ", get_marc_string(parse_item_to_dict(self.item))])

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

class Doc_1(models.Model):
    """
    Реализация с использованием Custom Fields для каждого элемента (slow)
    Список Документов
    Table with docs items. The Item Field in the DB hard coded in MARC format see https://bitbucket.org/voleg/bicat/wiki/Поле%20ITEM
    """
    doc_id = models.IntegerField("№ Документа", primary_key=True, db_column='DOC_ID')
    rectype = models.CharField("тип записи", max_length=1, db_column='RECTYPE', blank=True)
    biblevel = models.CharField("библиотечный уровень", max_length=1, db_column='BIBLEVEL', blank=True)
    item = models.TextField("документ в макроподобном формате", db_column='ITEM', blank=True)

    # Далее идут псевдо-поля извлекаемые из item
    item_author_main = MarcItemField("Авторы", help_text='основной автор', marc_tag='100', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_authors_other = MarcItemField("Другие авторы", marc_tag='700', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_last_change_timestamp = MarcItemField("Изменён", marc_tag='005', marc_subtag='0', db_column='ITEM', max_length=255, blank=True)
    item_faculty = MarcItemField("Кафедра", marc_tag='903', marc_subtag='d', db_column='ITEM', max_length=255, blank=True)
    item_source = MarcItemField("Источник поступления", marc_tag='901', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_speciality = MarcItemField("Специальность (направление)", marc_tag='903', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_type_work_program = MarcItemField("Вид", help_text='контрольная, лабораторная, рабочая программа', marc_tag='903', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_place_and_date_of_publication = MarcItemField("Место и дата издания", marc_tag='773', marc_subtag='d', db_column='ITEM', max_length=255, blank=True)
    item_other_information = MarcItemField("Прочая информация", marc_tag='773', marc_subtag='g', db_column='ITEM', max_length=255, blank=True)
    item_source_name = MarcItemField("Название источника", marc_tag='773', marc_subtag='t', db_column='ITEM', max_length=255, blank=True)
    item_entrence_date = MarcItemField("Дата поступления", marc_tag='990', marc_subtag='f', db_column='ITEM', max_length=255, blank=True)
    item_series = MarcItemField("Серия", marc_tag='440', db_column='ITEM', max_length=255, blank=True)
    item_ISBN = MarcItemField("ISBN", marc_tag='020', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_cost = MarcItemField("Цена", marc_tag='020', marc_subtag='c', db_column='ITEM', max_length=255, blank=True)
    item_bibliography = MarcItemField("Библиография", marc_tag='504', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_pages = MarcItemField("Объём издания", marc_tag='300', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_illustrations = MarcItemField("Илл./тип воспроизв.", marc_tag='300', marc_subtag='b', db_column='ITEM', max_length=255, blank=True)
    item_format = MarcItemField("Формат", marc_tag='300', marc_subtag='c', db_column='ITEM', max_length=255, blank=True)
    item_cover = MarcItemField("Вид переплета", marc_tag='300', marc_subtag='d', db_column='ITEM', max_length=255, blank=True)
    item_covering_matireals = MarcItemField("Сопров.мат", marc_tag='300', marc_subtag='e', db_column='ITEM', max_length=255, blank=True)
    item_shelving_index = MarcItemField("Полочн.индекс", marc_tag='090', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_cat_index = MarcItemField("Кат.индекс", marc_tag='090', marc_subtag='c', db_column='ITEM', max_length=255, blank=True)
    item_author_lable = MarcItemField("Авторский знак", marc_tag='090', marc_subtag='x', db_column='ITEM', max_length=255, blank=True)
    item_invent_code = MarcItemField("Инвентарный номер", marc_tag='090', marc_subtag='e', db_column='ITEM', max_length=255, blank=True)
    item_title = MarcItemField("Заглавие", marc_tag='245', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_next_title = MarcItemField("Продолж.заглавия", marc_tag='245', marc_subtag='b', db_column='ITEM', max_length=255, blank=True)
    item_responsibility = MarcItemField("Ответственность", marc_tag='245', marc_subtag='c', db_column='ITEM', max_length=255, blank=True)
    item_title_date_of_works = MarcItemField("Даты произведения", marc_tag='245', marc_subtag='f', db_column='ITEM', max_length=255, blank=True)
    item_title_media = MarcItemField("Носитель", marc_tag='245', marc_subtag='h', db_column='ITEM', max_length=255, blank=True)
    item_title_part_number = MarcItemField("Номер части", marc_tag='245', marc_subtag='n', db_column='ITEM', max_length=255, blank=True)
    item_title_parallel_title = MarcItemField("Паралельное заглавие", marc_tag='245', marc_subtag='o', db_column='ITEM', max_length=255, blank=True)
    item_title_part_name = MarcItemField("Название части", marc_tag='245', marc_subtag='p', db_column='ITEM', max_length=255, blank=True)
    item_title_version = MarcItemField("Версия", marc_tag='245', marc_subtag='s', db_column='ITEM', max_length=255, blank=True)
    item_publish = MarcItemField("Изд", marc_tag='260', db_column='ITEM', max_length=255, blank=True)
    item_place = MarcItemField("Место издания", marc_tag='260', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_publisher = MarcItemField("Издательство", marc_tag='260', marc_subtag='b', db_column='ITEM', max_length=255, blank=True)
    item_publication_year = MarcItemField("Дата издания", marc_tag='260', marc_subtag='c', db_column='ITEM', max_length=255, blank=True)
    item_remarks = MarcItemField("Примечание", marc_tag='500', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)
    item_tags = MarcItemField("Ключевые слова", marc_tag='653', marc_subtag='a', db_column='ITEM', max_length=255, blank=True)

    objects = ItemManager()
    item_name = lambda self, tag=None, subtag=None: get_marc_field(self.item, tag=tag, subtag=subtag)
    # ... Тут дальше крамешный ад, что делать, с которым пока непонял, так, что лепим пока так
    def item_author(self):
        """
        извлекаем Авторов из Item
        """
        author = get_marc_field(self.item, tag='100', subtag='a')
        other_authors = get_marc_field(self.item, tag='700', subtag='a')
        if author == "" or other_authors == "": splitter = u''
        else: splitter = u', '
        return splitter.join([author,other_authors])

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
    idx_id = models.ForeignKey("Idx100A", to_field='idx_id', primary_key=True, null=False, db_column='IDX_ID', blank=True)
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID')

    class Meta:
        auto_created = True
        db_table = u'IDX100aX'
        abstract = True


class Idx100A(models.Model):
    """ Словарь Авторов """
    idx_id = models.IntegerField(db_column='IDX_ID', unique=True)
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM')
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True)

    @models.permalink
    def get_absolute_url(self):
        name = '%s_authors' % (self._meta.app_label)
        return name, [self.idx_id]

    def __unicode__(self):
        return " ".join([unicode(self.term), unicode(self.cnt)])

    class Meta:
        verbose_name = u'Словарь Авторов'
        verbose_name_plural = u'Авторы'
        db_table = u'IDX100a'
        abstract = True


class Idx653Ax(models.Model):
    idx_id = models.ForeignKey("Idx653A", to_field='idx_id', primary_key=True, db_column=u'IDX_ID')
    doc_id = models.ForeignKey("Doc", db_column=u'DOC_ID')

    class Meta:
        auto_created = True
        db_table = u'IDX653aX'
        abstract = True


class Idx653A(models.Model):
    """ Словарь Тегов """
    idx_id = models.IntegerField(db_column='IDX_ID', unique=True)
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM')
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True)

    @models.permalink
    def get_absolute_url(self):
        name = '%s_tags' % (self._meta.app_label)
        return name, [self.idx_id]

    def __unicode__(self):
        return " ".join([unicode(self.term), unicode(self.cnt)])

    class Meta:
        verbose_name = u'Словарь Тегов'
        verbose_name_plural = u'Теги'
        db_table = u'IDX653a'
        abstract = True


class Idx245Ax(models.Model):
    idx_id = models.ForeignKey("Idx245A", to_field='idx_id', primary_key=True, null=False, db_column='IDX_ID', blank=True)
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID')

    class Meta:
        auto_created = True
        db_table = u'IDX245aX'
        abstract = True


class Idx245A(models.Model):
    """ Словарь Заглавий публикаций """
    idx_id = models.IntegerField(db_column='IDX_ID', unique=True)
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM')
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True)

    def __unicode__(self):
        return " ".join([unicode(self.term), unicode(self.cnt)])

    class Meta:
        verbose_name = u'Словарь Заглавий публикаций'
        verbose_name_plural = u'Заглавия'
        db_table = u'IDX245a'
        abstract = True


class Siglas(models.Model):
    id = models.IntegerField(primary_key=True, db_column=u'ID')
    fullname = models.CharField(max_length=255, db_column=u'FULLNAME', blank=True)
    shortname = models.CharField(max_length=255, unique=True, db_column=u'SHORTNAME', blank=True)

    class Meta:
        db_table = u'SIGLAS'
        abstract = True
        verbose_name = u'Сигла хранения'
        verbose_name_plural = u'Сиглы хранения'


class Metaidx(models.Model):
    """ Reflects a list of dictionaries created in MarcSQL """
    name = models.CharField("имя поля словаря", max_length=32, primary_key=True, db_column=u'NAME')
    type = models.CharField("Тип словаря", max_length=32, db_column=u'TYPE')
    maxlen = models.IntegerField("Длина поля", null=True, db_column=u'MAXLEN', blank=True)
    tags = models.CharField("коды подполей",  max_length=40, db_column=u'TAGS', blank=True)
    caption = models.CharField("название словаря", max_length=50, db_column=u'CAPTION', blank=True)
    sep = models.CharField("разделители", max_length=64, db_column=u'SEP', blank=True)

    def __unicode__(self):
        return ' '.join([unicode(self.caption), unicode(self.tags)])

    class Meta:
        verbose_name = u'внутренний словарь'
        verbose_name_plural = u'внутренние словари'
        db_table = u'METAIDX'
        abstract = True


class Idx260Cx(models.Model):
    idx = models.ForeignKey('Idx260C', to_field='idx_id', primary_key=True, db_column=u'IDX_ID', blank=True)
    doc_id = models.ForeignKey('Doc', db_column=u'DOC_ID')

    class Meta:
        abstract = True
        db_table = u'IDX260cX'


class Idx260C(models.Model):
    """ Index of Years of publish """
    idx_id = models.PositiveIntegerField(unique=True, db_column=u'IDX_ID')
    term = models.TextField(primary_key=True, db_column=u'TERM')
    cnt = models.IntegerField(null=True, db_column=u'CNT', blank=True)

    def __unicode__(self):
        return " ".join([unicode(self.term), unicode(self.cnt)])

    class Meta:
        verbose_name_plural = u'Даты издания'
        verbose_name = u'Дата издания'
        abstract = True
        db_table = u'IDX260c'