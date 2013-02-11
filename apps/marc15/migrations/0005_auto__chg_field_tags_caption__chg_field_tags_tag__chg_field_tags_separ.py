# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tags.caption'
        db.alter_column('marc15_tags', 'caption', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Tags.tag'
        db.alter_column('marc15_tags', 'tag', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'Tags.separator'
        db.alter_column('marc15_tags', 'separator', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'Tags.subtag'
        db.alter_column('marc15_tags', 'subtag', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

    def backwards(self, orm):

        # Changing field 'Tags.caption'
        db.alter_column('marc15_tags', 'caption', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # User chose to not deal with backwards NULL issues for 'Tags.tag'
        raise RuntimeError("Cannot reverse this migration. 'Tags.tag' and its values cannot be restored.")

        # Changing field 'Tags.separator'
        db.alter_column('marc15_tags', 'separator', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

        # Changing field 'Tags.subtag'
        db.alter_column('marc15_tags', 'subtag', self.gf('django.db.models.fields.CharField')(default='', max_length=1))

    models = {
        'marc15.tags': {
            'Meta': {'unique_together': "(('tag', 'subtag'),)", 'object_name': 'Tags'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'flags': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'separator': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'subtag': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['marc15']