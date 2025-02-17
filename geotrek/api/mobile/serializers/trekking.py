from __future__ import unicode_literals

import os
from django.conf import settings
from rest_framework import serializers
from rest_framework_gis import serializers as geo_serializers

from geotrek.api.mobile.serializers.tourism import InformationDeskSerializer
from geotrek.zoning.models import City, District

if 'geotrek.trekking' in settings.INSTALLED_APPS:
    from geotrek.trekking import models as trekking_models

    class POIListSerializer(geo_serializers.GeoFeatureModelSerializer):
        pictures = serializers.SerializerMethodField(read_only=True)
        geometry = geo_serializers.GeometryField(read_only=True, precision=7, source='geom2d_transformed')
        type = serializers.ReadOnlyField(source='type.pk')

        def get_pictures(self, obj):
            serialized = []
            for picture, thdetail in obj.resized_pictures:
                serialized.append({
                    'author': picture.author,
                    'title': picture.title,
                    'legend': picture.legend,
                    'url': os.path.join('/', str(self.context['trek_pk']), settings.MEDIA_URL[1:], thdetail.name),
                })
            return serialized

        class Meta:
            model = trekking_models.POI
            id_field = 'pk'
            geo_field = 'geometry'
            fields = (
                'id', 'pk', 'pictures', 'name', 'description', 'type', 'geometry',
            )

    class TrekBaseSerializer(geo_serializers.GeoFeatureModelSerializer):
        cities = serializers.SerializerMethodField(read_only=True)
        districts = serializers.SerializerMethodField(read_only=True)
        length = serializers.SerializerMethodField(read_only=True)
        departure_city = serializers.SerializerMethodField(read_only=True)

        def get_cities(self, obj):
            qs = City.objects.all()
            cities = qs.filter(geom__intersects=(obj.geom, 0))
            return cities.values_list('code', flat=True)

        def get_departure_city(self, obj):
            qs = City.objects.all()
            if obj.start_point:
                city = qs.filter(geom__covers=(obj.start_point, 0)).first()
                if city:
                    return city.code
            return None

        def get_length(self, obj):
            return round(obj.length_2d_m, 1)

        def get_districts(self, obj):
            qs = District.objects.all()
            districts = qs.filter(geom__intersects=(obj.geom, 0))
            return [district.pk for district in districts]

        class Meta:
            model = trekking_models.Trek
            id_field = 'pk'
            geo_field = 'geometry'

    class TrekDetailSerializer(TrekBaseSerializer):
        geometry = geo_serializers.GeometryField(read_only=True, precision=7, source='geom2d_transformed')
        pictures = serializers.ReadOnlyField(source='serializable_pictures_mobile')
        arrival_city = serializers.SerializerMethodField(read_only=True)
        information_desks = serializers.SerializerMethodField()
        parking_location = serializers.SerializerMethodField(read_only=True)
        profile = serializers.SerializerMethodField(read_only=True)
        points_reference = serializers.SerializerMethodField()

        def get_points_reference(self, obj):
            if not obj.points_reference:
                return None
            return obj.points_reference.transform(settings.API_SRID, clone=True).coords

        def get_parking_location(self, obj):
            if not obj.parking_location:
                return None
            return obj.parking_location.transform(settings.API_SRID, clone=True).coords

        def get_arrival_city(self, obj):
            qs = City.objects.all()
            if obj.end_point:
                city = qs.filter(geom__covers=(obj.end_point, 0)).first()
                if city:
                    return city.code
            return None

        def get_geometry(self, obj):
            return obj.geom2d_transformed

        def get_information_desks(self, obj):
            return [
                InformationDeskSerializer(information_desk, context={'trek_pk': obj.pk}).data
                for information_desk in obj.information_desks.all()
            ]

        def get_profile(self, obj):
            return os.path.join("/", str(obj.pk), settings.MEDIA_URL.lstrip('/'), obj.get_elevation_chart_url_png())

        class Meta(TrekBaseSerializer.Meta):
            auto_bbox = True
            fields = (
                'id', 'pk', 'name', 'slug', 'accessibilities', 'description_teaser', 'cities', 'profile',
                'description', 'departure', 'arrival', 'duration', 'access', 'advised_parking', 'advice',
                'difficulty', 'length', 'ascent', 'descent', 'route', 'is_park_centered', 'parking_location',
                'min_elevation', 'max_elevation', 'themes', 'networks', 'practice', 'difficulty',
                'geometry', 'pictures', 'information_desks', 'cities', 'departure_city', 'arrival_city',
                'points_reference', 'districts'
            )

    class TrekListSerializer(TrekBaseSerializer):
        first_picture = serializers.ReadOnlyField(source='resized_picture_mobile')
        geometry = geo_serializers.GeometryField(read_only=True, precision=7, source='start_point', )

        class Meta(TrekBaseSerializer.Meta):
            fields = (
                'id', 'pk', 'first_picture', 'name', 'departure', 'accessibilities', 'route', 'departure_city',
                'difficulty', 'practice', 'themes', 'length', 'geometry', 'districts', 'cities', 'duration', 'ascent',
                'descent',
            )
