from datetime import datetime, date, timedelta
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from logging import getLogger
from rest_framework import serializers

from .models import Client

logger = getLogger("clients.serializers")

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name')
        depth = 1