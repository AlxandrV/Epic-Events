from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

from event_api.permissions import IsAuthenticatedGetUser, IsAuthenticatedManageTeam
from event_api.models import SalesTeam, SupportTeam, ManageTeam
from event_api.serializers import UserSerializer, ManageTeamSerializer, ManageTeamDetailSerializer, SalesTeamSerializer, SalesTeamDetailSerializer, SupportTeamSerializer, SupportTeamDetailSerializer, ClientSerializer, ClientDetailSerializer, ContractSerializer, ContractDetailSerializer, EventSerializer, EventDetailSerializer


class RegisterView(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedGetUser]

    def update(self, request, *args, **kwargs):
        try:
            request.data._mutable = True
            request.data['password2'] = request.data['password']
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return self.serializer_class.log(self, e)

    def destroy(self, request, *args, **kwargs):
        print(request.user)
        return super().destroy(request, *args, **kwargs)


class ManageTeamView(ModelViewSet):

    queryset = ManageTeam.objects.all()
    serializer_class = ManageTeamSerializer
    detail_serializer_class = ManageTeamDetailSerializer
    permission_classes = [IsAuthenticatedManageTeam]

    def get_serializer_class(self):
        print()
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class SalesTeamView(ModelViewSet):

    queryset = SalesTeam.objects.all()
    serializer_class = SalesTeamSerializer
    detail_serializer_class = SalesTeamDetailSerializer
    permission_classes = [IsAuthenticatedManageTeam]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class SupportTeamView(ModelViewSet):

    queryset = SupportTeam.objects.all()
    serializer_class = SupportTeamSerializer
    detail_serializer_class = SupportTeamDetailSerializer
    permission_classes = [IsAuthenticatedManageTeam]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
