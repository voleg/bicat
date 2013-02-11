# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tags'
        db.create_table('marc15_tags', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('subtag', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('flags', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('separator', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal('marc15', ['Tags'])

        # Adding unique constraint on 'Tags', fields ['tag', 'subtag']
        db.create_unique('marc15_tags', ['tag', 'subtag'])


    def backwards(self, orm):
        # Removing unique constraint on 'Tags', fields ['tag', 'subtag']
        db.delete_unique('marc15_tags', ['tag', 'subtag'])

        # Deleting model 'Tags'
        db.delete_table('marc15_tags')


    models = {
        'marc15.tags': {
            'Meta': {'unique_together': "(('tag', 'subtag'),)", 'object_name': 'Tags'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'flags': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'separator': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'subtag': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['marc15']