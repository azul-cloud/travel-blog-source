# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'BlogEntryClick.user_name' to match new field type.
        db.rename_column('reports_blogentryclick', 'user_name', 'user_name_id')
        # Changing field 'BlogEntryClick.user_name'
        db.alter_column('reports_blogentryclick', 'user_name_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))
        # Adding index on 'BlogEntryClick', fields ['user_name']
        db.create_index('reports_blogentryclick', ['user_name_id'])


    def backwards(self, orm):
        # Removing index on 'BlogEntryClick', fields ['user_name']
        db.delete_index('reports_blogentryclick', ['user_name_id'])


        # Renaming column for 'BlogEntryClick.user_name' to match new field type.
        db.rename_column('reports_blogentryclick', 'user_name_id', 'user_name')
        # Changing field 'BlogEntryClick.user_name'
        db.alter_column('reports_blogentryclick', 'user_name', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'reports.blogentryclick': {
            'Meta': {'object_name': 'BlogEntryClick'},
            'blog_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.BlogEntry']", 'null': 'True', 'blank': 'True'}),
            'click_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'reports.blogsiteclick': {
            'Meta': {'object_name': 'BlogSiteClick'},
            'blog_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.BlogSite']", 'null': 'True', 'blank': 'True'}),
            'click_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'default': "'SEARCH'", 'max_length': '50'}),
            'sponsor_type': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '30'})
        },
        'travel.blogentry': {
            'Meta': {'ordering': "['-post_date']", 'object_name': 'BlogEntry'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blog_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.BlogSite']", 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Continent']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Country']", 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'travel.blogsite': {
            'Meta': {'ordering': "['site_name']", 'object_name': 'BlogSite'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'blog_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Continent']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Country']", 'null': 'True', 'blank': 'True'}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary_language': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'quick_info': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'sponsor_begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sponsor_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sponsor_level': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '30'}),
            'sponsor_type': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '30'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'travel.continent': {
            'Meta': {'ordering': "['display_value']", 'object_name': 'Continent'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_value': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'travel.country': {
            'Meta': {'ordering': "['display_value']", 'object_name': 'Country'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Continent']"}),
            'display_value': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['reports']