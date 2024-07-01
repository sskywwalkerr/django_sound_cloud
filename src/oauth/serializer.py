from rest_framework import serializers


class GoogleAuth(serializers.Serializer):
    """Сериализация данных от google"""
    email = serializers.EmailField()
    token = serializers.CharField()