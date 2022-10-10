from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from event_api.permissions import IsAuthenticatedGetClient
from event_api.models import Client
from event_api.serializers import ClientSerializer, ClientDetailSerializer


class ClientView(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [IsAuthenticatedGetClient]
    filter_backends = [filters.SearchFilter]
    search_fields = ('company_name', 'email')


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()