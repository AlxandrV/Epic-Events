from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from event_api.permissions import IsAuthenticatedGetContract
from event_api.models import Contract
from event_api.serializers import ContractSerializer, ContractDetailSerializer


class ContractView(ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsAuthenticatedGetContract]
    filter_backends = [filters.SearchFilter]
    search_fields = ('created_time', 'client__company_name', 'client__email')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()