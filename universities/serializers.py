from rest_framework import serializers
from universities.models import Universities


class UniversitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Universities
        fields = '__all__'