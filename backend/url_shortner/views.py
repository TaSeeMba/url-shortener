from rest_framework.generics import CreateAPIView
from .serializers import URLsSerializer


class ShortenUrlView(CreateAPIView):
    """
    Shorten url received in post body
    """
    serializer_class = URLsSerializer
