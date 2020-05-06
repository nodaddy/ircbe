# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from internships.models import Internships
from users.models import User
from django.core.mail import send_mail
from django.core import mail
from django.http import HttpResponse


class MyAccepted(APIView):
    def get(self, request):

        declared_projects = Internships.objects.filter(status='DC')
        for proje in declared_projects:
            email_string = proje.space_seperated_emails_of_selected_students
            email_list = email_string.split(' ')
            for e_mail in email_list:
                if request.user.email == e_mail:
                    title_look_up_3 = request.user.my_accepted.split('~')
                    proje_title = proje.title
                    if proje_title not in title_look_up_3:
                        request.user.my_accepted += proje.title + "~"
        app_array = request.user.my_applications.split("~")
        acc_array = request.user.my_accepted.split("~")

        for pro in acc_array:
            if pro in app_array:
                app_array.remove(pro)
                string_to_set_app = "~"
                for pro in app_array:
                    if pro != "":
                        string_to_set_app += pro + "~"
                        request.user.my_applications = string_to_set_app
                        request.user.save()

        str_to_ret = ""
        title_look_up_2 = request.user.my_accepted.split('~')
        for tit in title_look_up_2:
            if tit != "":
                proj = Internships.objects.filter(title=tit)
                #print()
                str_to_ret += proj.values('title')[0]['title'] + "*" + proj.values('university')[0]['university'] + "*" + str(proj.values('deadline')[0]['deadline']) + "~"

        return HttpResponse(str_to_ret)


class MyApplications(APIView):
    def get(self, request):
        str_to_ret = ""
        title_look_up_0 = request.user.my_applications.split('~')
        for tit in title_look_up_0:
            if tit != "":
                proj = Internships.objects.filter(title=tit, status='OP')
                #print()
                str_to_ret += proj.values('title')[0]['title'] + "*" + proj.values('university')[0]['university'] + "*" + str(proj.values('deadline')[0]['deadline']) + "~"

        return HttpResponse(str_to_ret)

class ApplyToTheProject(APIView):
    def post(self, request):

        # request.user.my_applications=""
        # request.user.save()

        title_look_up_1 = request.user.my_applications.split('~')
        project_title = request.data['pTitle']
        if project_title not in title_look_up_1:
            pemail = Internships.objects.filter(title=project_title)
            stuff = pemail.values('contact_email')
            #print(stuff[0]['contact_email']) DO_NOT_EDIT

            internship_email = stuff[0]['contact_email']
            proposal_text = request.data['proposal']
            student_name = request.user.name
            student_email = request.user.email
            student_mobile = request.user.phone
            student_resume = request.user.cv

            #SEND AN EMAIL


            my_app_string = request.user.my_applications + request.data['pTitle'] + "~"
            request.user.my_applications = my_app_string

            request.user.save()

        else:
            print("user has already submitted for this project")






            # app_string = cs_list_app + request.data['title_of_project'] + "~"
            #request.user.my_applications = app_string
            #request.user.save()

        return Response({})


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
