#coding: utf-8
from django.db import models
from managers import ItemManager
from parse import parse_item_to_dict, get_marc_string, get_marc_field, get_tag_name, ListToStr
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