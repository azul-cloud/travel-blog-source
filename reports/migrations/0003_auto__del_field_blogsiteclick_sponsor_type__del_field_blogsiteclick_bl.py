# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BlogSiteClick.sponsor_type'
        db.delete_column('reports_blogsiteclick', 'sponsor_type_id')

        # Deleting field 'BlogSiteClick.blog_site'
        db.delete_column('reports_blogsiteclick', 'blog_site_id')

        # Deleting field 'BlogEntryClick.blog_entry'
        db.delete_column('reports_blogentryclick', 'blog_entry_id')


    def backwards(self, orm):
        # Adding field 'BlogSiteClick.sponsor_type'
        db.add_column('reports_blogsiteclick', 'sponsor_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['travel.SponsorType']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'BlogSiteClick.blog_site'
        raise RuntimeError("Cannot reverse this migration. 'BlogSiteClick.blog_site' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'BlogEntryClick.blog_entry'
        raise RuntimeError("Cannot reverse this migration. 'BlogEntryClick.blog_entry' and its values cannot be restored.")

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
            'location': ('django.db.models.fields.CharField', [], {'default': "'SEARCH'", 'max_length': '50'})
        }
    }

    complete_apps = ['reports']