from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .models import SalesTeam, SupportTeam, ManageTeam, Client, Contract, Event
from event_api.serializers import UserSerializer, ManageTeamSerializer, ManageTeamDetailSerializer, SalesTeamSerializer, SalesTeamDetailSerializer, SupportTeamSerializer, SupportTeamDetailSerializer, ClientSerializer, ClientDetailSerializer, ContractSerializer, ContractDetailSerializer, EventSerializer, EventDetailSerializer
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
    detail_serializer_class = ManageTeamDetailSerializer

    def get_serializer_class(self):
        print()
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class SalesTeamView(ModelViewSet):

    queryset = SalesTeam.objects.all()
    serializer_class = SalesTeamSerializer
    detail_serializer_class = SalesTeamDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class SupportTeamView(ModelViewSet):

    queryset = SupportTeam.objects.all()
    serializer_class = SupportTeamSerializer
    detail_serializer_class = SupportTeamDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ClientView(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    detail_serializer_class = ClientDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ContractView(ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    detail_serializer_class = ContractDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
            

class EventView(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    detail_serializer_class = EventDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        contract = Contract.objects.get(id=request.data['event_status'])
        if contract.status == False:
            return self.serializer_class.log(self, 'Le statut du contract ne permet pas la création de l\'évènement.')
        return super().create(request, *args, **kwargs)