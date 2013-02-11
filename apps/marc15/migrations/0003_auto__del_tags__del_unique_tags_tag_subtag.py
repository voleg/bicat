# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Tags', fields ['tag', 'subtag']
        db.delete_unique('marc15_tags', ['TAG', 'SUBTAG'])

        # Deleting model 'Tags'
        db.delete_table('marc15_tags')


    def backwards(self, orm):
        # Adding model 'Tags'
        db.create_table('marc15_tags', (
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=3, primary_key=True, db_column='TAG')),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=40, db_column='CAPTION', blank=True)),
            ('flags', self.gf('django.db.models.fields.IntegerField')(null=True, db_column='FLAGS', blank=True)),
            ('subtag', self.gf('django.db.models.fields.CharField')(max_length=1, db_column='SUBTAG', blank=True)),
            ('separator', self.gf('django.db.models.fields.CharField')(max_length=1, db_column='SEPARATOR', blank=True)),
        ))
        db.send_create_signal('marc15', ['Tags'])

        # Adding unique constraint on 'Tags', fields ['tag', 'subtag']
        db.create_unique('marc15_tags', ['TAG', 'SUBTAG'])


    models = {
        
    }

    complete_apps = ['marc15']