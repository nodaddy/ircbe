from django.shortcuts import render
from rest_framework.views import APIView
from internships.models import Internships
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers

seperator = '%next%'

# Create your views here.
class ListInternships(APIView):
    def get(self, request):
        jsonStuff = serializers.serialize("json", Internships.objects.filter(status='OP'))
        #print(jsonStuff)
        data={'jsonStuff':jsonStuff}
        return JsonResponse(data)

class FRPResults(APIView):
    def get(self, request):
        jsonStuff = serializers.serialize("json", Internships.objects.filter(status='DC'))
        data={'jsonStuff':jsonStuff}
        return JsonResponse(data)

class ListBookmarks(APIView):
    def get(self, request):
        listt = request.user.my_bookmarks.split(seperator)
        internships_list = []
        for tit in listt:
            if tit!="" and tit!=" ":
                internship = Internships.objects.get(title=tit)
                internships_list.append(internship)
        jsonStuff = serializers.serialize("json", internships_list)
        #print(jsonStuff)
        data={'jsonStuff':jsonStuff}
        return JsonResponse(data)