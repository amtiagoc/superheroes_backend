
from django.db.models import fields
from rest_framework import serializers
from .models import Superheroe

class SuperheroeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Superheroe
        fields = '__all__'

