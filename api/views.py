from django.shortcuts import render
from rest_framework import viewsets
from .models import PerevalAdded
from .serializers import PerevalSerializer
# Create your views here.


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = PerevalAdded.objects.all()
    serializer_class = PerevalSerializer
