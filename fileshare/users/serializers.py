from rest_framework import serializers
# from .models import Profile
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4)
    class Meta:
        model = User
        fields = ['username','email','password']
		
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        
        token = super().get_token(user)
        print("Token",token)
        token['username'] = user.username
        print("Token",token)
        token['email'] = user.email
        print("Token",token)
        return token


# class ProfileSerializer(serializers.ModelSerializer):
	
# 	class Meta:
# 		model = Profile
# 		fields = ['user', 'image', 'slug', 'bio','friends']