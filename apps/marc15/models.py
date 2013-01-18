#coding: utf-8
from django.db import models
from managers import ItemManager
from parse import parse_item_to_dict, get_marc_string, get_caption, get_marc_field
class MarcField(models.TextField):
    pass

class Tag(models.Model):
    tag = models.CharField("номер поля (марковкском формате)", max_length=3, primary_key=True, db_column='TAG')
    subtag = models.CharField("буква подполя", max_length=1, unique=True, db_column='SUBTAG')
    flags = models.IntegerField("Флаги", null=True, db_column='FLAGS', blank=True)
    separator = models.CharField("Разделитель", max_length=1, db_column='SEPARATOR', blank=True)
    caption = models.CharField("Наименование", max_length=40, db_column='CAPTION', blank=True)

    def __unicode__(self):
        return self.tag + self.subtag + " " + self.caption
    class Meta:
        unique_together = (("tag", "subtag"),)
        db_table = u'TAG'
        abstract = True
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'

# Table with docs items. The Item Field in the DB hard coded in MARC format see https://bitbucket.org/voleg/bicat/wiki/Поле%20ITEM
class Doc(models.Model):
    doc_id = models.IntegerField("№ Документа", primary_key=True, db_column='DOC_ID')
    rectype = models.CharField("тип записи", max_length=1, db_column='RECTYPE', blank=True)
    biblevel = models.CharField("библиотечный уровень", max_length=1, db_column='BIBLEVEL', blank=True)
    item = models.TextField("документ в макроподобном формате", db_column='ITEM', blank=True)
    objects = ItemManager()

    def item_author(self):
        author = get_marc_field(self.item, tag='100', subtag='a')
        other_authors = get_marc_field(self.item, tag='700', subtag='a')
        return ''.join([author,',',other_authors])

    def item_changetimestamp(self):
        timestamp = get_marc_field(self.item, tag='005', subtag='0')[:14]
        return timestamp

    def item_dict_full(self):
        return "".join([str(self.doc_id),": ",get_marc_string(parse_item_to_dict(self.item))])

    def item_dict(self):
        return ''.join([self.item_dict_full()[:600], ' ...'])

    def __unicode__(self):
        return str(self.doc_id) + " " + self.item[:80]

    class Meta:
        db_table = u'DOC'
        abstract = True
        verbose_name = u'Документ'
        verbose_name_plural = u'Документы'

class Idx100A(models.Model):
    idx_id = models.IntegerField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX100a'
        abstract = True

class Idx100Ax(models.Model):
    idx_id = models.IntegerField(primary_key=True, null=False, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX100aX'
        abstract = True

class Idx653A(models.Model):
    idx_id = models.IntegerField(db_column='IDX_ID') # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX653a'
        abstract = True

class Idx245A(models.Model):
    idx_id = models.IntegerField(db_column='IDX_ID',) # Field name made lowercase.
    term = models.CharField(max_length=255, primary_key=True, db_column='TERM') # Field name made lowercase.
    cnt = models.IntegerField(null=True, db_column='CNT', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'IDX245a'
        abstract = True

class Idx245Ax(models.Model):
    idx_id = models.IntegerField(primary_key=True, null=False, db_column='IDX_ID', blank=True) # Field name made lowercase.
    doc_id = models.ForeignKey("Doc", db_column='DOC_ID') # Field name made lowercase.
    class Meta:
        db_table = u'IDX245aX'
        abstract = True
