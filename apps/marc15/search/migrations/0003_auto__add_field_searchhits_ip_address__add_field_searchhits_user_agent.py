# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SearchHits.ip_address'
        db.add_column('search_searchhits', 'ip_address',
                      self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SearchHits.user_agent'
        db.add_column('search_searchhits', 'user_agent',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SearchHits.ip_address'
        db.delete_column('search_searchhits', 'ip_address')

        # Deleting field 'SearchHits.user_agent'
        db.delete_column('search_searchhits', 'user_agent')


    models = {
        'search.searchhits': {
            'Meta': {'object_name': 'SearchHits'},
            'created': ('apps.utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'modified': ('apps.utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['search']