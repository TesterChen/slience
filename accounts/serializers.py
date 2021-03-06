from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator



class UserSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=6,write_only=True)

    def validate_email(self,value):
        if not value.endswith("@pxn.one"):
            raise serializers.ValidationError('Must use company mailbox')
        return value


    def create(self,validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('url','email','password')