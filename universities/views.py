from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from universities.models import Universities
from universities.serializers import UniversitiesSerializers


class UniversitiesViewSet(ModelViewSet):
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializers
