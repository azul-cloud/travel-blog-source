# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Country.views'
        db.add_column('travel_country', 'views',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Continent.views'
        db.add_column('travel_continent', 'views',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Country.views'
        db.delete_column('travel_country', 'views')

        # Deleting field 'Continent.views'
        db.delete_column('travel_continent', 'views')


    models = {
        'travel.continent': {
            'Meta': {'ordering': "['display_value']", 'object_name': 'Continent'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_value': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'views': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'travel.country': {
            'Meta': {'ordering': "['display_value']", 'object_name': 'Country'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Continent']"}),
            'display_value': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'views': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['travel']