from rest_framework.authtoken import views
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^list/', ListInternships.as_view()),
    url(r'^results/', FRPResults.as_view()),
    url(r'^bookmarks/', ListBookmarks.as_view()),


]