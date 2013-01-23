__author__ = 'voleg'
from django.db.models import SubfieldBase, CharField, TextField

class TagSubtagField(CharField):

    def get_internal_type(self):
        return "CharField"

    def to_python(self, value):
        if isinstance(value, basestring) or value is None:
            return value
        return unicode(value)

    def get_prep_value(self, value):
        return self.to_python(value)

class Item_AuthorsField(TextField):
    pass