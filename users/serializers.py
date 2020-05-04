import re
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth import authenticate
from users.models import User
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)

        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise serializers.ValidationError(msg)
        attrs['user'] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    newpassword = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            year=validated_data['year'],
            enrl_no=validated_data['enrl_no'],
            phone=validated_data['phone'],
            skype=validated_data['skype'],
            dept=validated_data['dept'],
            cv=validated_data['cv'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('email', 'name', 'year', 'enrl_no', 'phone', 'skype', 'dept', 'cv', 'password')
