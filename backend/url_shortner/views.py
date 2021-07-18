import json
from django.conf import settings
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from .models import URLs
from .serializers import URLsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
ACCESS_TOKEN = settings.BITLY_TOKEN


def format_url(url_string):
    # add the trailing slash required by django url fields
    return url_string if url_string.endswith("/") else url_string + "/"


@api_view(['POST'])
def shorten_url(request):
    """
    Shorten url received in post body
    """
    try:
        with transaction.atomic():
            long_url = request.data['long_url']
            formatted_long_url = format_url(long_url)
            if URLs.objects.filter(full_url__iexact=formatted_long_url).exists():
                stored_url = URLs.objects.get(full_url=formatted_long_url)
                serializer = URLsSerializer(stored_url)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                url = URLs(full_url=formatted_long_url)
                url.save()
                serializer = URLsSerializer(url)
                return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_400_BAD_REQUEST)
