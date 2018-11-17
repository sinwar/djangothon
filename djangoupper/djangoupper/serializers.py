# generated serializers
from djangoupper.models import *
from rest_framework import serializers
class LocalDetailSerializer(serializers.ModelSerializer):
  # detail serializer
  class Meta:
    model = Local
    fields = []

class LocalCreateUpdateSerializer(serializers.ModelSerializer):
  # create update serializer
  class Meta:
    model = Local
    fields = []

class UserProfileDetailSerializer(serializers.ModelSerializer):
  # detail serializer
  class Meta:
    model = UserProfile
    fields = []

class UserProfileCreateUpdateSerializer(serializers.ModelSerializer):
  # create update serializer
  class Meta:
    model = UserProfile
    fields = []

