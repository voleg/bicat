# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'SearchHits.referer'
        db.alter_column('search_searchhits', 'referer', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True))

    def backwards(self, orm):

        # Changing field 'SearchHits.referer'
        db.alter_column('search_searchhits', 'referer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    models = {
        'search.searchhits': {
            'Meta': {'object_name': 'SearchHits'},
            'created': ('apps.utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'modified': ('apps.utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['search']