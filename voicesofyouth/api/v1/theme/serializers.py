from rest_framework import serializers

from voicesofyouth.api.v1.serializers import VoySerializer
from voicesofyouth.theme.models import Theme


class ThemeSerializer(VoySerializer):
    tags = serializers.HyperlinkedRelatedField(
        read_only=True,
        many=True,
        view_name='tags-detail'
    )
    project = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='projects-detail'
    )

    class Meta:
        model = Theme
        fields = (
            'project',
            'bounds',
            'name',
            'description',
            'tags',
            'color',
        )


# class ThemeSerializer(serializers.ModelSerializer):
#     languages = serializers.SerializerMethodField()
#     tags = serializers.SerializerMethodField()
#     url = serializers.SerializerMethodField()
#     reports = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Theme
#         fields = ('id', 'url', 'name', 'project', 'visible', 'languages', 'tags', 'reports')
#
#     def get_languages(self, obj):
#         return ThemeTranslationSerializer(obj.get_languages(), many=True).data
#
#     def get_tags(self, obj):
#         return TagSerializer(obj.get_tags(), many=True).data
#
#     def get_url(self, obj):
#         return reverse('themes-detail', kwargs={'pk': obj.id})
#
#     def get_reports(self, obj):
#         return obj.get_total_reports()
