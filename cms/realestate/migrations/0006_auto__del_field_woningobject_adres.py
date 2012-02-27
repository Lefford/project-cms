# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'WoningObject.adres'
        db.delete_column('realestate_woningobject', 'adres')


    def backwards(self, orm):
        
        # Adding field 'WoningObject.adres'
        db.add_column('realestate_woningobject', 'adres', self.gf('cms.utils.models.AutoCompleteField')(default=None, max_length=255), keep_default=False)


    models = {
        'realestate.woningobject': {
            'Meta': {'object_name': 'WoningObject'},
            'build_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '31'}),
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'prijs': ('django.db.models.fields.IntegerField', [], {}),
            'rooms': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tumbs_pics': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['realestate']