# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field portal on 'Trek'
        m2m_table_name = 'o_r_itineraire_portal'
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trek', models.ForeignKey(orm[u'trekking.trek'], null=False)),
            ('targetportal', models.ForeignKey(orm[u'common.targetportal'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trek_id', 'targetportal_id'])


    def backwards(self, orm):
        # Removing M2M table for field portal on 'Trek'
        db.delete_table('o_r_itineraire_portal')


    models = {
        u'authent.structure': {
            'Meta': {'ordering': "['name']", 'object_name': 'Structure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'cirkwi.cirkwilocomotion': {
            'Meta': {'ordering': "['name']", 'object_name': 'CirkwiLocomotion', 'db_table': "'o_b_cirkwi_locomotion'"},
            'eid': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"})
        },
        u'cirkwi.cirkwipoicategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'CirkwiPOICategory', 'db_table': "'o_b_cirkwi_poi_category'"},
            'eid': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"})
        },
        u'cirkwi.cirkwitag': {
            'Meta': {'ordering': "['name']", 'object_name': 'CirkwiTag', 'db_table': "'o_b_cirkwi_tag'"},
            'eid': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"})
        },
        u'common.recordsource': {
            'Meta': {'ordering': "['name']", 'object_name': 'RecordSource', 'db_table': "'o_b_source_fiche'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'", 'blank': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'db_column': "'website'", 'blank': 'True'})
        },
        u'common.targetportal': {
            'Meta': {'ordering': "('name',)", 'object_name': 'TargetPortal', 'db_table': "'o_b_target_portal'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '50'}),
            'website': ('django.db.models.fields.URLField', [], {'unique': "'True'", 'max_length': '256', 'db_column': "'website'"})
        },
        u'common.theme': {
            'Meta': {'ordering': "['label']", 'object_name': 'Theme', 'db_table': "'o_b_theme'"},
            'cirkwi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cirkwi.CirkwiTag']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'theme'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"})
        },
        u'core.comfort': {
            'Meta': {'ordering': "['comfort']", 'object_name': 'Comfort', 'db_table': "'l_b_confort'"},
            'comfort': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'confort'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.network': {
            'Meta': {'ordering': "['network']", 'object_name': 'Network', 'db_table': "'l_b_reseau'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'reseau'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.path': {
            'Meta': {'object_name': 'Path', 'db_table': "'l_t_troncon'"},
            'arrival': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'db_column': "'arrivee'", 'blank': 'True'}),
            'ascent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'denivelee_positive'", 'blank': 'True'}),
            'comfort': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'db_column': "'confort'", 'to': u"orm['core.Comfort']"}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'db_column': "'remarques'", 'blank': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'date_insert'", 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'date_update'", 'blank': 'True'}),
            'departure': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'null': 'True', 'db_column': "'depart'", 'blank': 'True'}),
            'descent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'denivelee_negative'", 'blank': 'True'}),
            'eid': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_column': "'id_externe'", 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '2154', 'spatial_index': 'False'}),
            'geom_3d': ('django.contrib.gis.db.models.fields.GeometryField', [], {'default': 'None', 'dim': '3', 'spatial_index': 'False', 'null': 'True', 'srid': '2154'}),
            'geom_cadastre': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '2154', 'null': 'True', 'spatial_index': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_column': "'longueur'", 'blank': 'True'}),
            'max_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'altitude_maximum'", 'blank': 'True'}),
            'min_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'altitude_minimum'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'db_column': "'nom'", 'blank': 'True'}),
            'networks': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'paths'", 'to': u"orm['core.Network']", 'db_table': "'l_r_troncon_reseau'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'slope': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_column': "'pente'", 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'db_column': "'source'", 'to': u"orm['core.PathSource']"}),
            'stake': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'paths'", 'null': 'True', 'db_column': "'enjeu'", 'to': u"orm['core.Stake']"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"}),
            'usages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'paths'", 'to': u"orm['core.Usage']", 'db_table': "'l_r_troncon_usage'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'valide'"}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_column': "'visible'"})
        },
        u'core.pathaggregation': {
            'Meta': {'ordering': "['order']", 'object_name': 'PathAggregation', 'db_table': "'e_r_evenement_troncon'"},
            'end_position': ('django.db.models.fields.FloatField', [], {'db_column': "'pk_fin'", 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'ordre'", 'blank': 'True'}),
            'path': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'aggregations'", 'on_delete': 'models.DO_NOTHING', 'db_column': "'troncon'", 'to': u"orm['core.Path']"}),
            'start_position': ('django.db.models.fields.FloatField', [], {'db_column': "'pk_debut'", 'db_index': 'True'}),
            'topo_object': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'aggregations'", 'db_column': "'evenement'", 'to': u"orm['core.Topology']"})
        },
        u'core.pathsource': {
            'Meta': {'ordering': "['source']", 'object_name': 'PathSource', 'db_table': "'l_b_source_troncon'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.stake': {
            'Meta': {'ordering': "['id']", 'object_name': 'Stake', 'db_table': "'l_b_enjeu'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stake': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'enjeu'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"})
        },
        u'core.topology': {
            'Meta': {'object_name': 'Topology', 'db_table': "'e_t_evenement'"},
            'ascent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'denivelee_positive'", 'blank': 'True'}),
            'date_insert': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_column': "'date_insert'", 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'date_update'", 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'supprime'"}),
            'descent': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'denivelee_negative'", 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.GeometryField', [], {'default': 'None', 'srid': '2154', 'null': 'True', 'spatial_index': 'False'}),
            'geom_3d': ('django.contrib.gis.db.models.fields.GeometryField', [], {'default': 'None', 'dim': '3', 'spatial_index': 'False', 'null': 'True', 'srid': '2154'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'length': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_column': "'longueur'", 'blank': 'True'}),
            'max_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'altitude_maximum'", 'blank': 'True'}),
            'min_elevation': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'db_column': "'altitude_minimum'", 'blank': 'True'}),
            'offset': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'db_column': "'decallage'"}),
            'paths': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Path']", 'through': u"orm['core.PathAggregation']", 'db_column': "'troncons'", 'symmetrical': 'False'}),
            'slope': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'db_column': "'pente'", 'blank': 'True'})
        },
        u'core.usage': {
            'Meta': {'ordering': "['usage']", 'object_name': 'Usage', 'db_table': "'l_b_usage'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"}),
            'usage': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "'usage'"})
        },
        u'tourism.informationdesk': {
            'Meta': {'ordering': "['name']", 'object_name': 'InformationDesk', 'db_table': "'t_b_renseignement'"},
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'", 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '256', 'null': 'True', 'db_column': "'email'", 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2154', 'null': 'True', 'spatial_index': 'False', 'db_column': "'geom'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipality': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'db_column': "'commune'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'db_column': "'nom'"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'db_column': "'telephone'", 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'photo'", 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'db_column': "'code'", 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'db_column': "'rue'", 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'desks'", 'db_column': "'type'", 'to': u"orm['tourism.InformationDeskType']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'db_column': "'website'", 'blank': 'True'})
        },
        u'tourism.informationdesktype': {
            'Meta': {'ordering': "['label']", 'object_name': 'InformationDeskType', 'db_table': "'t_b_type_renseignement'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'label'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"})
        },
        u'trekking.accessibility': {
            'Meta': {'ordering': "['name']", 'object_name': 'Accessibility', 'db_table': "'o_b_accessibilite'"},
            'cirkwi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cirkwi.CirkwiTag']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'", 'blank': 'True'})
        },
        u'trekking.difficultylevel': {
            'Meta': {'ordering': "['id']", 'object_name': 'DifficultyLevel', 'db_table': "'o_b_difficulte'"},
            'cirkwi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cirkwi.CirkwiTag']", 'null': 'True', 'blank': 'True'}),
            'cirkwi_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'niveau_cirkwi'", 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'difficulte'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'", 'blank': 'True'})
        },
        u'trekking.orderedtrekchild': {
            'Meta': {'ordering': "('parent__id', 'order')", 'unique_together': "(('parent', 'child'),)", 'object_name': 'OrderedTrekChild', 'db_table': "'o_r_itineraire_itineraire2'"},
            'child': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trek_parents'", 'to': u"orm['trekking.Trek']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trek_children'", 'to': u"orm['trekking.Trek']"})
        },
        u'trekking.poi': {
            'Meta': {'object_name': 'POI', 'db_table': "'o_t_poi'", '_ormbases': [u'core.Topology']},
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'"}),
            'eid': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_column': "'id_externe'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'date_publication'", 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'public'"}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'relecture'"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"}),
            'topo_object': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Topology']", 'unique': 'True', 'primary_key': 'True', 'db_column': "'evenement'"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pois'", 'db_column': "'type'", 'to': u"orm['trekking.POIType']"})
        },
        u'trekking.poitype': {
            'Meta': {'ordering': "['label']", 'object_name': 'POIType', 'db_table': "'o_b_poi'"},
            'cirkwi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cirkwi.CirkwiPOICategory']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"})
        },
        u'trekking.practice': {
            'Meta': {'ordering': "['order', 'name']", 'object_name': 'Practice', 'db_table': "'o_b_pratique'"},
            'cirkwi': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cirkwi.CirkwiLocomotion']", 'null': 'True', 'blank': 'True'}),
            'distance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'distance'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'tri'", 'blank': 'True'}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"})
        },
        u'trekking.route': {
            'Meta': {'ordering': "['route']", 'object_name': 'Route', 'db_table': "'o_b_parcours'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'", 'blank': 'True'}),
            'route': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'parcours'"})
        },
        u'trekking.service': {
            'Meta': {'object_name': 'Service', 'db_table': "'o_t_service'", '_ormbases': [u'core.Topology']},
            'eid': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_column': "'id_externe'", 'blank': 'True'}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"}),
            'topo_object': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Topology']", 'unique': 'True', 'primary_key': 'True', 'db_column': "'evenement'"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'services'", 'db_column': "'type'", 'to': u"orm['trekking.ServiceType']"})
        },
        u'trekking.servicetype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ServiceType', 'db_table': "'o_b_service'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"}),
            'practices': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'services'", 'to': u"orm['trekking.Practice']", 'db_table': "'o_r_service_pratique'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'date_publication'", 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'public'"}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'relecture'"})
        },
        u'trekking.trek': {
            'Meta': {'ordering': "['name']", 'object_name': 'Trek', 'db_table': "'o_t_itineraire'", '_ormbases': [u'core.Topology']},
            'access': ('django.db.models.fields.TextField', [], {'db_column': "'acces'", 'blank': 'True'}),
            'accessibilities': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'treks'", 'to': u"orm['trekking.Accessibility']", 'db_table': "'o_r_itineraire_accessibilite'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'advice': ('django.db.models.fields.TextField', [], {'db_column': "'recommandation'", 'blank': 'True'}),
            'advised_parking': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'parking'", 'blank': 'True'}),
            'ambiance': ('django.db.models.fields.TextField', [], {'db_column': "'ambiance'", 'blank': 'True'}),
            'arrival': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'arrivee'", 'blank': 'True'}),
            'departure': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'depart'", 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'db_column': "'description'", 'blank': 'True'}),
            'description_teaser': ('django.db.models.fields.TextField', [], {'db_column': "'chapeau'", 'blank': 'True'}),
            'difficulty': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'treks'", 'null': 'True', 'db_column': "'difficulte'", 'to': u"orm['trekking.DifficultyLevel']"}),
            'disabled_infrastructure': ('django.db.models.fields.TextField', [], {'db_column': "'handicap'", 'blank': 'True'}),
            'duration': ('django.db.models.fields.FloatField', [], {'default': '0', 'db_column': "'duree'", 'blank': 'True'}),
            'eid': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_column': "'id_externe'", 'blank': 'True'}),
            'eid2': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'db_column': "'id_externe2'", 'blank': 'True'}),
            'information_desks': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'treks'", 'to': u"orm['tourism.InformationDesk']", 'db_table': "'o_r_itineraire_renseignement'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'is_park_centered': ('django.db.models.fields.BooleanField', [], {'db_column': "'coeur'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'networks': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'treks'", 'to': u"orm['trekking.TrekNetwork']", 'db_table': "'o_r_itineraire_reseau'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'parking_location': ('django.contrib.gis.db.models.fields.PointField', [], {'srid': '2154', 'null': 'True', 'spatial_index': 'False', 'db_column': "'geom_parking'", 'blank': 'True'}),
            'points_reference': ('django.contrib.gis.db.models.fields.MultiPointField', [], {'srid': '2154', 'null': 'True', 'spatial_index': 'False', 'db_column': "'geom_points_reference'", 'blank': 'True'}),
            'portal': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'treks'", 'blank': 'True', 'db_table': "'o_r_itineraire_portal'", 'to': u"orm['common.TargetPortal']"}),
            'practice': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'treks'", 'null': 'True', 'db_column': "'pratique'", 'to': u"orm['trekking.Practice']"}),
            'public_transport': ('django.db.models.fields.TextField', [], {'db_column': "'transport'", 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'date_publication'", 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'public'"}),
            'related_treks': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_treks+'", 'symmetrical': 'False', 'through': u"orm['trekking.TrekRelationship']", 'to': u"orm['trekking.Trek']"}),
            'review': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'relecture'"}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'treks'", 'null': 'True', 'db_column': "'parcours'", 'to': u"orm['trekking.Route']"}),
            'source': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'treks'", 'blank': 'True', 'db_table': "'o_r_itineraire_source'", 'to': u"orm['common.RecordSource']"}),
            'structure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authent.Structure']", 'db_column': "'structure'"}),
            'themes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'treks'", 'to': u"orm['common.Theme']", 'db_table': "'o_r_itineraire_theme'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'topo_object': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Topology']", 'unique': 'True', 'primary_key': 'True', 'db_column': "'evenement'"}),
            'web_links': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'treks'", 'to': u"orm['trekking.WebLink']", 'db_table': "'o_r_itineraire_web'", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'})
        },
        u'trekking.treknetwork': {
            'Meta': {'ordering': "['network']", 'object_name': 'TrekNetwork', 'db_table': "'o_b_reseau'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'reseau'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"})
        },
        u'trekking.trekrelationship': {
            'Meta': {'unique_together': "(('trek_a', 'trek_b'),)", 'object_name': 'TrekRelationship', 'db_table': "'o_r_itineraire_itineraire'"},
            'has_common_departure': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'depart_commun'"}),
            'has_common_edge': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'troncons_communs'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_circuit_step': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'etape_circuit'"}),
            'trek_a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trek_relationship_a'", 'db_column': "'itineraire_a'", 'to': u"orm['trekking.Trek']"}),
            'trek_b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trek_relationship_b'", 'db_column': "'itineraire_b'", 'to': u"orm['trekking.Trek']"})
        },
        u'trekking.weblink': {
            'Meta': {'ordering': "['name']", 'object_name': 'WebLink', 'db_table': "'o_t_web'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'links'", 'null': 'True', 'db_column': "'categorie'", 'to': u"orm['trekking.WebLinkCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '2048', 'db_column': "'url'"})
        },
        u'trekking.weblinkcategory': {
            'Meta': {'ordering': "['label']", 'object_name': 'WebLinkCategory', 'db_table': "'o_b_web_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'db_column': "'nom'"}),
            'pictogram': ('django.db.models.fields.files.FileField', [], {'max_length': '512', 'null': 'True', 'db_column': "'picto'"})
        }
    }

    complete_apps = ['trekking']