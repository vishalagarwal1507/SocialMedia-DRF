from rest_framework import serializers
# from .models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4,write_only=True)
    class Meta:
        model = User
        fields = ['username','email','password']
		
        
# class ProfileSerializer(serializers.ModelSerializer):
	
# 	class Meta:
# 		model = Profile
# 		fields = ['user', 'image', 'slug', 'bio','friends']