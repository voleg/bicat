#coding: utf-8
from django.db import models
from django.contrib.contenttypes.models import ContentType
from managers import ItemManager
from fields import ItemField

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
    marc_indexed_authors = models.ManyToManyField('Idx100A', through='Idx100Ax', verbose_name='Авторы')
    marc_indexed_tags = models.ManyToManyField('Idx653A', through='Idx653Ax', verbose_name='Теги')
    marc_indexed_titles = models.ManyToManyField('Idx245A', through='Idx245Ax', verbose_name='Заглавия')
    marc_indexed_years = models.ManyToManyField('Idx260C', through='Idx260Cx', verbose_name='Даты публикаций')
    marc_indexed_publishers = models.ManyToManyField('Idx260B', through='Idx260Bx', verbose_name='Издательства')
    marc_indexed_sourcename = models.ManyToManyField('Idx773T', through='Idx773Tx', verbose_name='Названия Источников')

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

    @models.permalink
    def get_absolute_url(self):
        name = '%s_authors' % (self._meta.app_label)
        return name, [self.idx_id]

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

    @models.permalink
    def get_absolute_url(self):
        name = '%s_authors' % (self._meta.app_label)
        return name, [self.idx_id]

    def __unicode__(self):
        return " ".join([unicode(self.term), unicode(self.cnt)])

    class Meta:
        verbose_name_plural = u'Даты издания'
        verbose_name = u'Дата издания'
        abstract = True
        db_table = u'IDX260c'


class Idx260B(models.Model):
    """ Издательства """
    idx_id = models.PositiveIntegerField(unique=True, db_column=u'IDX_ID')
    term = models.TextField(primary_key=True, db_column=u'TERM')
    cnt = models.IntegerField(null=True, db_column=u'CNT', blank=True)

    class Meta:
        abstract = True
        db_table = u'IDX260b'


class Idx260Bx(models.Model):
    idx_id = models.ForeignKey('Idx260B', to_field='idx_id', primary_key=True, null=False, db_column='IDX_ID', blank=True)
    doc_id = models.ForeignKey('Doc', db_column=u'DOC_ID')

    class Meta:
        abstract = True
        db_table = u'IDX260bX'


class Idx773Tx(models.Model):
    idx_id = models.ForeignKey('Idx773T', to_field='idx_id', null=True, db_column=u'IDX_ID', blank=True)
    doc_id = models.ForeignKey("Doc", db_column=u'DOC_ID')

    class Meta:
        abstract = True
        db_table = u'IDX773tX'


class Idx773T(models.Model):
    """ Index Dictionary of sources"""
    idx_id = models.PositiveIntegerField(db_column=u'IDX_ID', unique=True)
    term = models.CharField(max_length=255, primary_key=True, db_column=u'TERM')
    cnt = models.IntegerField(null=True, db_column=u'CNT', blank=True)

    def __unicode__(self):
        return " ".join([unicode(self.term), unicode(self.cnt)])

    class Meta:
        abstract = True
        verbose_name = u'Название источника'
        verbose_name_plural = u'Источники'
        db_table = u'IDX773t'