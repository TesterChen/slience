from django.shortcuts import render
from rest_framework import viewsets
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
    def get_queryset(self):
        return None