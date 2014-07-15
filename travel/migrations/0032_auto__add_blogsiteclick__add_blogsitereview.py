# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogSiteClick'
        db.create_table('travel_blogsiteclick', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.BlogSite'])),
            ('click_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('travel', ['BlogSiteClick'])

        # Adding model 'BlogSiteReview'
        db.create_table('travel_blogsitereview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.BlogSite'])),
            ('review_rating', self.gf('django.db.models.fields.IntegerField')()),
            ('sponsor_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.SponsorLevel'])),
            ('review_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('travel', ['BlogSiteReview'])


    def backwards(self, orm):
        # Deleting model 'BlogSiteClick'
        db.delete_table('travel_blogsiteclick')

        # Deleting model 'BlogSiteReview'
        db.delete_table('travel_blogsitereview')


    models = {
        'travel.blogentry': {
            'Meta': {'ordering': "['-post_date']", 'object_name': 'BlogEntry'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Country']"}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'post_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'views': ('django.db.models.fields.IntegerField', [], {})
        },
        'travel.blogentryclick': {
            'Meta': {'object_name': 'BlogEntryClick'},
            'blog_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.BlogEntry']"}),
            'click_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'travel.blogowner': {
            'Meta': {'object_name': 'BlogOwner'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'travel.blogsite': {
            'Meta': {'ordering': "['site_name']", 'object_name': 'BlogSite'},
            'blog_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.BlogOwner']"}),
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Continent']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Country']"}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quick_info': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'sponsor_begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sponsor_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sponsor_level': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['travel.SponsorLevel']", 'symmetrical': 'False'}),
            'sponsor_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'travel.blogsiteclick': {
            'Meta': {'object_name': 'BlogSiteClick'},
            'blog_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.BlogSite']"}),
            'click_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'travel.blogsitereview': {
            'Meta': {'object_name': 'BlogSiteReview'},
            'blog_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.BlogSite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'review_rating': ('django.db.models.fields.IntegerField', [], {}),
            'sponsor_level': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.SponsorLevel']"})
        },
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
        },
        'travel.faq': {
            'Meta': {'object_name': 'faq'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'travel.sponsorlevel': {
            'Meta': {'object_name': 'SponsorLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor_level': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['travel']