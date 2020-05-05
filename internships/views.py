from django.shortcuts import render
from rest_framework.views import APIView
from internships.models import Internships
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
class ListInternships(APIView):
    def get(self, request):
        jsonStuff = serializers.serialize("json", Internships.objects.all())
        #print(jsonStuff)
        data={'jsonStuff':jsonStuff}
        return JsonResponse(data)
