from django.contrib.auth.models import User

from auths.serializers import UserSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# for retrieving all users
class UsersView(generics.ListAPIView):

    permission_classes = (IsAuthenticated, IsAdminUser, )

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return UserSerializer
