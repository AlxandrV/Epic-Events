from rest_framework.viewsets import ModelViewSet

from event_api.models import Contract
from event_api.serializers import ContractSerializer, ContractDetailSerializer


class ContractView(ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    detail_serializer_class = ContractDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()