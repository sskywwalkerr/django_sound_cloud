from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ('avatar', 'country', 'city', 'bio', 'display_name')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AuthUser
        fields = ('id', 'avatar', 'country', 'city', 'bio', 'display_name')

class GoogleAuth(serializers.Serializer):
    """Сериализация данных от google"""
    email = serializers.EmailField()
    token = serializers.CharField()

class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialLink
        fields = ('link',)
    """"""