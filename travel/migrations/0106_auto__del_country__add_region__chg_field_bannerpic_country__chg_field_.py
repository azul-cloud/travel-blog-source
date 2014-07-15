# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('travel_country')

        # Adding model 'Region'
        db.create_table('travel_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('display_value', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('image_alt', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('image_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('continent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Continent'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('blog_entry_pay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('banner_pic_pay', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('travel', ['Region'])


        # Changing field 'BannerPic.country'
        db.alter_column('travel_bannerpic', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Region'], null=True))

        # Changing field 'BlogEntry.country'
        db.alter_column('travel_blogentry', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Region'], null=True))

        # Changing field 'BlogSite.country'
        db.alter_column('travel_blogsite', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Region'], null=True))

    def backwards(self, orm):
        # Adding model 'Country'
        db.create_table('travel_country', (
            ('views', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('banner_pic_pay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('blog_entry_pay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image_alt', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('display_value', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('continent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Continent'])),
        ))
        db.send_create_signal('travel', ['Country'])

        # Deleting model 'Region'
        db.delete_table('travel_region')


        # Changing field 'BannerPic.country'
        db.alter_column('travel_bannerpic', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Country'], null=True))

        # Changing field 'BlogEntry.country'
        db.alter_column('travel_blogentry', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Country'], null=True))

        # Changing field 'BlogSite.country'
        db.alter_column('travel_blogsite', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Country'], null=True))

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
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Continent']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Region']", 'null': 'True', 'blank': 'True'}),
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
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Region']", 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'travel.blogsite': {
            'Meta': {'ordering': "['site_name']", 'object_name': 'BlogSite'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'blog_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Continent']", 'null': 'True', 'blank': 'True'}),
            'continent_sponsor_begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'continent_sponsor_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'continent_sponsor_type': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '30'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Region']", 'null': 'True', 'blank': 'True'}),
            'country_sponsor_begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'country_sponsor_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'country_sponsor_type': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '30'}),
            'create_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'primary_language': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'quick_info': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'twitter_id': ('django.db.models.fields.CharField', [], {'max_length': "'30'", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'travel.blogsitereview': {
            'Meta': {'ordering': "['-review_date']", 'object_name': 'BlogSiteReview'},
            'blog_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.BlogSite']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'review_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'review_rating': ('django.db.models.fields.IntegerField', [], {}),
            'sponsor_type': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '30'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'travel.continent': {
            'Meta': {'ordering': "['display_value']", 'object_name': 'Continent'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banner_pic_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blog_entry_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'display_value': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
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
        'travel.region': {
            'Meta': {'ordering': "['display_value']", 'object_name': 'Region'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banner_pic_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'blog_entry_pay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['travel.Continent']"}),
            'display_value': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'travel.sponsorlevel': {
            'Meta': {'object_name': 'SponsorLevel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor_level': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'travel.sponsortype': {
            'Meta': {'object_name': 'SponsorType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor_type': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['travel']