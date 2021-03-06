from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
# Create your views here.
from rest_framework_jwt.settings import api_settings

from rest_framework_jwt import views

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'currentAuthority': 'user',
    }
# views.jwt_response_payload_handler=jwt_response_payload_handler

# api_settings.JWT_RESPONSE_PAYLOAD_HANDLER=jwt_response_payload_handler


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
    # def get_queryset(self,request):
    #     return request.user.objects.all()

    def list(self,request):
        # user = request.user
        # serializer = UserSerializer(user)
        # return Response(serializer.data)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)