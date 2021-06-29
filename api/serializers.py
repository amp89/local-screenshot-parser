from .models import ScreenshotParse
from django.contrib.auth.models import User
from rest_framework import serializers

class ScreenshotParseSerializer(serializers.ModelSerializer):        
    class Meta:
        model = ScreenshotParse
        fields = ['id', 'path', 'text']

