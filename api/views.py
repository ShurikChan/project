from rest_framework import viewsets
from .models import Pereval
from .serializers import *

# Create your views here.


class ImageViewSet(viewsets.ModelViewSet):
    queryset = PerevalImages.objects.all()
    serializer_class = ImageSerializer


class CoordViewSet(viewsets.ModelViewSet):
    queryset = PerevalCoords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = PerevalLevels.objects.all()
    serializer_class = LevelSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = PerevalUsers.objects.all()
    serializer_class = UserSerializer
