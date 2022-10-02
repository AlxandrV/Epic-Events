from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

from .models import SalesTeam, SupportTeam, ManageTeam
from .serializers import UserSerializer, ManageTeamSerializer
# Create your views here.

class RegisterView(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        try:
            request.data._mutable = True
            request.data['password2'] = request.data['password']
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return self.serializer_class.log(self, e)


class ManageTeamView(ModelViewSet):

    queryset = ManageTeam.objects.all()
    serializer_class = ManageTeamSerializer