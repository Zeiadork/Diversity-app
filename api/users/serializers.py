# from django.contrib.auth.models import User
from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'is_verified', 'banned', 'mind_state']