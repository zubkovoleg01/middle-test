from rest_framework import serializers
from app.models import PhoneNumber


class PhoneNumberInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'operator', 'region']