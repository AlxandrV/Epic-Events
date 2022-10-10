from rest_framework.viewsets import ModelViewSet

from event_api.models import Contract, Event
from event_api.permissions import IsAuthenticatedGetEvent
from event_api.serializers import EventSerializer, EventDetailSerializer


class EventView(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [IsAuthenticatedGetEvent]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        contract = Contract.objects.get(id=request.data['event_status'])
        if contract.status == False:
            return self.serializer_class.log(self, 'Le statut du contract ne permet pas la création de l\'évènement.')
        return super().create(request, *args, **kwargs)