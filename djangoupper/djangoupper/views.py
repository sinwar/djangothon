from rest_framework.generics import *
from djangoupper.models import *
from .serializers import *
class LocalListAPIView(ListAPIView):
  # list api view
  queryset = Local.objects.all()
  serializer_class = LocalDetailSerializer

class LocalDetailAPIView(RetrieveAPIView):
  # detail api view
  queryset = Local.objects.all()
  serializer_class = LocalDetailSerializer

class LocalCreateAPIView(CreateAPIView):
  # create api view
  queryset = Local.objects.all()
  serializer_class = LocalCreateUpdateSerializer

class LocalUpdateAPIView(UpdateAPIView):
  # update api view
  queryset = Local.objects.all()
  serializer_class = LocalCreateUpdateSerializer

class LocalDeleteAPIView(DestroyAPIView):
  # delete api view
  queryset = Local.objects.all()
  serializer_class = LocalDetailSerializer

class UserProfileListAPIView(ListAPIView):
  # list api view
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileDetailSerializer

class UserProfileDetailAPIView(RetrieveAPIView):
  # detail api view
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileDetailSerializer

class UserProfileCreateAPIView(CreateAPIView):
  # create api view
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileCreateUpdateSerializer

class UserProfileUpdateAPIView(UpdateAPIView):
  # update api view
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileCreateUpdateSerializer

class UserProfileDeleteAPIView(DestroyAPIView):
  # delete api view
  queryset = UserProfile.objects.all()
  serializer_class = UserProfileDetailSerializer

