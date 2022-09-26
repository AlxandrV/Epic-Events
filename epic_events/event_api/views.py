from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet
# Create your views here.

class RegisterView(ModelViewSet):

    queryset = User.objects.all()