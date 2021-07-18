from rest_framework import serializers
from .models import URLs
from django.db import transaction
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404

import re


def is_validate_url(url):
    # validate whether the supplied tring is valid url format
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def format_url(url_string):
    # add the trailing slash required by django url fields
    return url_string if url_string.endswith("/") else url_string + "/"


class URLsSerializer(serializers.ModelSerializer):
    full_url = serializers.URLField(read_only=True)
    url_hash = serializers.URLField(read_only=True)
    clicks = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = URLs
        fields = ('full_url', 'url_hash', 'clicks', 'created_at')

    def validate(self, attrs):
        data = super(URLsSerializer, self).validate(attrs)
        long_url = self.context['request'].data['long_url']
        if not is_validate_url(long_url):
            raise ValidationError('Supplied url is not a valid uri format')
        return data

    def create(self, validated_data):
        with transaction.atomic():
            long_url = self.context['request'].data['long_url']
            formatted_long_url = format_url(long_url)
            if URLs.objects.filter(full_url__iexact=formatted_long_url).exists():
                stored_url = get_object_or_404(URLs, full_url__iexact=formatted_long_url)
                return stored_url
            else:
                url = URLs(full_url=formatted_long_url)
                url.save()
                return url
