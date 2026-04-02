# from rest_framework import serializers
# from .models import Student

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__' # This grabs all fields (name, email, etc.)
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student

# Your existing student serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 

# NEW: Registration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # This ensures the password is never sent back in the API response
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        # We use create_user so Django securely hashes the password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user