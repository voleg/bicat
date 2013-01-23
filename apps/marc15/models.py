#coding: utf-8
from django.db import models
from managers import ItemManager
from parse import parse_item_to_dict, get_marc_string, get_caption, get_marc_field, item_timestamp_format
from fields import TagSubtagField

class MarcField(models.TextField):
    pass

class Tag(models.Model):
    tag = models.CharField("номер поля (марковкском формате)", max_length=3, primary_key=True, db_column='TAG')
    subtag = models.CharField("буква подполя", max_length=1, unique=True, db_column='SUBTAG')
    flags = models.IntegerField("Флаги", null=True, db_column='FLAGS', blank=True)
    separator = models.CharField("Разделитель", max_length=1, db_column='SEPARATOR', blank=True)
    caption = models.CharField("Наименование", max_length=40, db_column='CAPTION', blank=True)

    def __unicode__(self):
        return " ".join([self.tag, self.subtag, self.caption])
    class Meta:
        unique_together = (("tag", "subtag"),)
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
    objects = ItemManager()

    item_name = lambda self, tag=None, subtag=None: get_marc_field(self.item, tag=tag, subtag=subtag)
    # ... Тут дальше крамешный ад, что делать, с которым пока непонял, так, что лепим пока так

    def item_author(self):
        """извлекаем Авторов из Item"""
        author = get_marc_field(self.item, tag='100', subtag='a')
        other_authors = get_marc_field(self.item, tag='700', subtag='a')
        if author == "" or other_authors == "": splitter = u''
        else: splitter = u' ,'
        return splitter.join([author,other_authors])

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
    def item_pages(self):
        """Объём издания"""
        return get_marc_field(self.item, tag='300', subtag='a')
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

    def item_title(self):
        """
        245
            a	Заглавие:
                Инвестиции
            b	Продолж.заглавия:
                Учебник
            c	Ответственность:
                Пер. с англ.
                ...
        """
        return get_marc_field(self.item, tag='245')

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
        return " ".join([str(self.doc_id), self.item_author(), self.item_title()[:80]])

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

class Idx653A(models.Model):
    """ Словарь Тегов """
    idx_id = models.ForeignKey(Idx653Ax, db_column='IDX_ID')
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