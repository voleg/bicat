# coding: utf-8
from apps.marc15.models import *


class DocInv(DocInv):
    pass


class DocInvOff(DocInvOff):
    pass


class Doc(Doc):
    marc_indexed_sourcename = models.ManyToManyField('Idx773T', through='Idx773Tx', verbose_name='Словарь источников')
    marc_indexed_years = None
    pass


class Tag(Tag):
    pass


class Inv(Inv):
    pass


class Invoff(Invoff):
    pass


class Idx100Ax(Idx100Ax):
    pass


class Idx245Ax(Idx245Ax):
    pass


class Idx653Ax(Idx653Ax):
    pass


class Idx100A(Idx100A):
    pass


class Idx245A(Idx245A):
    pass


class Idx653A(Idx653A):
    pass


class Idx773Tx(models.Model):
    idx_id = models.ForeignKey('Idx773T', to_field='idx_id', null=True, db_column=u'IDX_ID', blank=True)
    doc_id = models.ForeignKey("Doc", db_column=u'DOC_ID')

    class Meta:
        db_table = u'IDX773tX'


class Idx773T(models.Model):
    """ Index Dictionary of sources"""
    idx_id = models.PositiveIntegerField(db_column=u'IDX_ID', unique=True)
    term = models.CharField(max_length=255, primary_key=True, db_column=u'TERM')
    cnt = models.IntegerField(null=True, db_column=u'CNT', blank=True)

    def __unicode__(self):
        return " ".join([unicode(self.term), unicode(self.cnt)])

    class Meta:
        verbose_name = u'Название источника'
        verbose_name_plural = u'Источники'
        db_table = u'IDX773t'

class Siglas(Siglas):
    pass


class Metaidx(Metaidx):
    pass


class Idx260C(Idx260C):
    pass


class Idx260Cx(Idx260Cx):
    pass
