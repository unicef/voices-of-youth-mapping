from rest_framework import serializers

from voicesofyouth.user.models import User


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    is_mapper = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'language', 'avatar', 'username', 'is_mapper')

    def get_avatar(self, obj):
        request = self.context['request']
        return request.build_absolute_uri(obj.get_avatar_display())

    def get_is_mapper(self, obj):
        return obj.is_mapper(obj)
