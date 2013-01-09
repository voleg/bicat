#coding: utf-8
from django.db import models
from managers import ItemManager

class Tag(models.Model):
    """
    Таблица TAG
    TAG-номер поля (марковкском формате)
    SUBTAG-буква подполя
    CAPTION-наименование поля(подполя)
    """
    tag = models.CharField(max_length=3, primary_key=True, db_column='TAG') # Field name made lowercase.
    subtag = models.CharField(max_length=1, unique=True, db_column='SUBTAG') # Field name made lowercase.
    flags = models.IntegerField(null=True, db_column='FLAGS', blank=True) # Field name made lowercase.
    separator = models.CharField(max_length=1, db_column='SEPARATOR', blank=True) # Field name made lowercase.
    caption = models.CharField(max_length=40, db_column='CAPTION', blank=True) # Field name made lowercase.
    def __unicode__(self):
        return self.tag + self.subtag + " " + self.caption
    class Meta:
        unique_together = (("tag", "subtag"),)
        db_table = u'TAG'
        abstract = True

# Table with docs items. The Item Field in the DB hard coded in MARC format see https://bitbucket.org/voleg/bicat/wiki/Поле%20ITEM
class Doc(models.Model):
    """
    Таблица DOC
    DOC_ID-идентификатор документа
    RECTYPE-тип записи
    BIBLEVEL-библиотечный уровень
    ITEM-документ в макроподобном формате
    """
    doc_id = models.IntegerField(primary_key=True, db_column='DOC_ID') # Field name made lowercase.
    rectype = models.CharField(max_length=1, db_column='RECTYPE', blank=True) # Field name made lowercase.
    biblevel = models.CharField(max_length=1, db_column='BIBLEVEL', blank=True) # Field name made lowercase.
    item = models.TextField(db_column='ITEM', blank=True) # Field name made lowercase.

    objects = ItemManager()

    def __unicode__(self):
        return str(self.doc_id) + " " + self.item[:80]
    class Meta:
        db_table = u'DOC'
        abstract = True

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
