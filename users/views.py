# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

class GetProfileData(APIView):
    def get(self, request):
        content = {
            'name': request.user.name,
            'dept': request.user.dept,
            'enrol_no': request.user.enrl_no,
            'email': request.user.email,
            'year': request.user.year,
            'phone': request.user.phone,
            'skype': request.user.skype,
            'cv': request.user.cv,

        }
        return Response(content)

class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        content = {
            'token': token.key,
            'full_name': user.get_full_name(),
            'short_name': user.get_short_name(),
            'email': user.email,
        }
        return Response(content)


class LogoutView(APIView):
    def get(self, request):
        content = {
            'status': 'Successfully Logged Out',
        }
        return Response(content)


class ChangePassword(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(email=User.objects.get(id=request.user.id).email, password=request.POST['password'])
            if not user:
                content = {
                    'status': 'Invalid Credentials',
                }
                return Response(content, status=status.HTTP_403_FORBIDDEN)
            else:
                user.set_password(request.POST['newpassword'])
                user.save()
                content = {
                    'status': 'Password Changed Successfully'
                }
                return Response(content)
        else:
            return Response(RegisterSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    permission_classes = ()
    password = serializers.CharField(write_only=True)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            content = {
                'token': token.key,
                'full_name': user.get_full_name(),
                'short_name': user.get_short_name(),
                'email': user.email,
            }
            return Response(content)
        else:
            return Response(RegisterSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
