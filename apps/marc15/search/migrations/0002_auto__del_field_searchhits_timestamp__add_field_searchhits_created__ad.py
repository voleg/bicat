# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'SearchHits.timestamp'
        db.delete_column('search_searchhits', 'timestamp')

        # Adding field 'SearchHits.created'
        db.add_column('search_searchhits', 'created',
                      self.gf('apps.utils.fields.AutoCreatedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'SearchHits.modified'
        db.add_column('search_searchhits', 'modified',
                      self.gf('apps.utils.fields.AutoLastModifiedField')(default=datetime.datetime.now),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'SearchHits.timestamp'
        db.add_column('search_searchhits', 'timestamp',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 3, 11, 0, 0), max_length=255, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SearchHits.created'
        db.delete_column('search_searchhits', 'created')

        # Deleting field 'SearchHits.modified'
        db.delete_column('search_searchhits', 'modified')


    models = {
        'search.searchhits': {
            'Meta': {'object_name': 'SearchHits'},
            'created': ('apps.utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('apps.utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['search']