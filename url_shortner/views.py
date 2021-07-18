from rest_framework.generics import CreateAPIView
from .serializers import URLsSerializer
from .models import URLs
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404


class ShortenUrlView(CreateAPIView):
    """
    Shorten url received in post body
    """
    serializer_class = URLsSerializer


@api_view(['GET'])
def decode(request, url_hash):
    url = get_object_or_404(URLs, url_hash=url_hash)
    url.clicked()
    serializer = URLsSerializer(url)
    return Response(serializer.data, status=status.HTTP_200_OK)
