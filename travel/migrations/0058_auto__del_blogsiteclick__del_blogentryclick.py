# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BlogSiteClick'
        db.delete_table('travel_blogsiteclick')

        # Deleting model 'BlogEntryClick'
        db.delete_table('travel_blogentryclick')


    def backwards(self, orm):
        # Adding model 'BlogSiteClick'
        db.create_table('travel_blogsiteclick', (
            ('blog_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.BlogSite'])),
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('location', self.gf('django.db.models.fields.CharField')(default='SEARCH', max_length=50)),
            ('click_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('travel', ['BlogSiteClick'])

        # Adding model 'BlogEntryClick'
        db.create_table('travel_blogentryclick', (
            ('click_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.BlogEntry'])),
        ))
        db.send_create_signal('travel', ['BlogEntryClick'])


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
        'travel.bannerpic': {
            'Meta': {'object_name': 'BannerPic'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
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
            'sponsor_level': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['travel.SponsorLevel']", 'null': 'True', 'blank': 'True'}),
            'sponsor_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'views': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
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
            'views': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'travel.error': {
            'Meta': {'object_name': 'Error'},
            'error_desc': ('django.db.models.fields.CharField', [], {'max_length': "'30'"}),
            'error_text': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'travel.feedback': {
            'Meta': {'ordering': "['submit_date']", 'object_name': 'Feedback'},
            'feedback': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'submit_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'travel.helptopic': {
            'Meta': {'ordering': "['group', 'sub_group', 'question_order']", 'object_name': 'HelpTopic'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'answer': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'question_order': ('django.db.models.fields.IntegerField', [], {}),
            'sub_group': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'travel.sponsorlevel': {
            'Meta': {'object_name': 'SponsorLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor_level': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['travel']