from rest_framework import viewsets, status
from .models import Pereval
from .serializers import *
from django.http import HttpResponse
# from rest_framework.generics import UpdateAPIView
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

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        return super().partial_update(request, *args, **kwargs) if instance.status =='new' else HttpResponse('Cannot update a completed pereval', status=status.HTTP_403_FORBIDDEN)


