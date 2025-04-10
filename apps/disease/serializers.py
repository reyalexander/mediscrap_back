from rest_framework import serializers
from .models import Disease, DiseaseRecord

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = '__all__'

class DiseaseRecordSerializer(serializers.ModelSerializer):
    disease = DiseaseSerializer(read_only=True)

    class Meta:
        model = DiseaseRecord
        fields = '__all__'
