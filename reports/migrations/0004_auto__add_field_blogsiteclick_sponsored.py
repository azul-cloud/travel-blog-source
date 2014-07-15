# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogSiteClick.sponsored'
        db.add_column('reports_blogsiteclick', 'sponsored',
                      self.gf('django.db.models.fields.CharField')(default='hi', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogSiteClick.sponsored'
        db.delete_column('reports_blogsiteclick', 'sponsored')


    models = {
        'reports.blogentryclick': {
            'Meta': {'object_name': 'BlogEntryClick'},
            'click_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'reports.blogsiteclick': {
            'Meta': {'object_name': 'BlogSiteClick'},
            'click_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'SEARCH'", 'max_length': '50'}),
            'sponsored': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['reports']