from rest_framework import serializers
from .models import UserScan

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserScan
        fields=('chest','waist','hipps','inseem','arm')