from rest_framework import serializers as rest_serializers

from geotrek.flatpages import models as flatpages_models
from geotrek.common.serializers import (
    TranslatedModelSerializer, BasePublishableSerializerMixin, RecordSourceSerializer
)


class FlatPageSerializer(BasePublishableSerializerMixin, TranslatedModelSerializer):
    slug = rest_serializers.Field(source='slug')
    last_modified = rest_serializers.Field(source='date_update')
    media = rest_serializers.Field(source='parse_media')
    source = RecordSourceSerializer()

    class Meta:
        model = flatpages_models.FlatPage
        fields = ('id', 'title', 'external_url', 'content', 'target',
                  'last_modified', 'slug', 'media', 'source') + \
            BasePublishableSerializerMixin.Meta.fields
