from rest_framework.authtoken import views
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/', LoginView.as_view()),
    url(r'^logout/', LogoutView.as_view()),
    url(r'^changepwd/', ChangePassword.as_view()),
    url(r'^register/', RegisterView.as_view()),
    url(r'^getprofile/', GetProfileData.as_view()),
]

