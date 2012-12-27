__author__ = 'voleg'

db_list = ('bicat', 'bikart', 'biuml')
app_list = ('BiCat', 'BiKart', 'BiUML')
class BiRouter(object):
    def db_for_read(self, model, **hints):

        if model._meta.app_label == 'BiUML':
            return 'biuml'
        elif model._meta.app_label == 'BiCat':
            return 'bicat'
        elif model._meta.app_label == 'BiKart':
            return 'bikart'

        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'BiUML':
            return 'biuml'
        elif model._meta.app_label == 'BiCat':
            return 'bicat'
        elif model._meta.app_label == 'BiKart':
            return 'bikart'

        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        for TheApp in app_list:
            if obj1._meta.app_label == TheApp and obj2._meta.app_label == TheApp:
                return True
            # Allow if neither is chinook app
            elif TheApp not in [obj1._meta.app_label, obj2._meta.app_label]:
                return True
        return None

    def allow_syncdb(self, db, model):

        if db in db_list:
            return None
        else:
            return None