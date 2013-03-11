# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SearchHits'
        db.create_table('search_searchhits', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 11, 0, 0), max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('search', ['SearchHits'])


    def backwards(self, orm):
        # Deleting model 'SearchHits'
        db.delete_table('search_searchhits')


    models = {
        'search.searchhits': {
            'Meta': {'object_name': 'SearchHits'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 11, 0, 0)', 'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['search']