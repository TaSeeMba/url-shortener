
from rest_framework import serializers
from .models import URLs


class URLsSerializer(serializers.ModelSerializer):
    full_url = serializers.URLField(read_only=True)
    url_hash = serializers.URLField(read_only=True)
    clicks = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = URLs
        fields = ('full_url', 'url_hash', 'clicks', 'created_at')