from django.contrib.auth.models import User
from rest_framework import serializers


#
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(required=False, max_length=30)
#     first_name = serializers.CharField(required=False, max_length=30)
#     last_name = serializers.CharField(required=False, max_length=30)
#     email = serializers.EmailField(required=False)
#
#     def create(self, validated_data):
#         return User.objects.create_user(
#             username=validated_data["username"],
#             email=validated_data["email"],
#             password="1234poiu"
#     )
#
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.email = validated_data.get('email', instance.email)
#
#         instance.save()
#         return instance


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email","is_superuser",'is_staff']
