# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'BlogEntrySiteClick'
        db.delete_table('travel_blogentrysiteclick')

        # Deleting model 'SponsorLevel'
        db.delete_table('travel_sponsorlevel')

        # Deleting model 'BlogEntry'
        db.delete_table('travel_blogentry')

        # Deleting model 'BlogSiteReview'
        db.delete_table('travel_blogsitereview')

        # Deleting model 'BlogEntryClick'
        db.delete_table('travel_blogentryclick')

        # Deleting model 'BlogSiteClick'
        db.delete_table('travel_blogsiteclick')

        # Deleting model 'BlogSite'
        db.delete_table('travel_blogsite')

        # Removing M2M table for field sponsor_level on 'BlogSite'
        db.delete_table(db.shorten_name('travel_blogsite_sponsor_level'))


    def backwards(self, orm):
        # Adding model 'BlogEntrySiteClick'
        db.create_table('travel_blogentrysiteclick', (
            ('click_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.BlogEntry'])),
        ))
        db.send_create_signal('travel', ['BlogEntrySiteClick'])

        # Adding model 'SponsorLevel'
        db.create_table('travel_sponsorlevel', (
            ('sponsor_level', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('travel', ['SponsorLevel'])

        # Adding model 'BlogEntry'
        db.create_table('travel_blogentry', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('views', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('post_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Country'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
        ))
        db.send_create_signal('travel', ['BlogEntry'])

        # Adding model 'BlogSiteReview'
        db.create_table('travel_blogsitereview', (
            ('review_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('blog_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.BlogSite'])),
            ('review_rating', self.gf('django.db.models.fields.IntegerField')()),
            ('sponsor_level', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.SponsorLevel'])),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('travel', ['BlogSiteReview'])

        # Adding model 'BlogEntryClick'
        db.create_table('travel_blogentryclick', (
            ('click_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.BlogEntry'])),
        ))
        db.send_create_signal('travel', ['BlogEntryClick'])

        # Adding model 'BlogSiteClick'
        db.create_table('travel_blogsiteclick', (
            ('click_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blog_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.BlogSite'])),
        ))
        db.send_create_signal('travel', ['BlogSiteClick'])

        # Adding model 'BlogSite'
        db.create_table('travel_blogsite', (
            ('sponsor_end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('create_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('sponsor_type', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('sponsor_begin_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('site_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.Country'])),
            ('blog_owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['travel.BlogOwner'])),
            ('quick_info', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('travel', ['BlogSite'])

        # Adding M2M table for field sponsor_level on 'BlogSite'
        m2m_table_name = db.shorten_name('travel_blogsite_sponsor_level')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blogsite', models.ForeignKey(orm['travel.blogsite'], null=False)),
            ('sponsorlevel', models.ForeignKey(orm['travel.sponsorlevel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blogsite_id', 'sponsorlevel_id'])


    models = {
        'travel.blogowner': {
            'Meta': {'object_name': 'BlogOwner'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
        }
    }

    complete_apps = ['travel']