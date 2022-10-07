from rest_framework import serializers

from event_api.models import Contract, SupportTeam, Event
from .management import SupportTeamDetailSerializer
from .contracts import ContractDetailSerializer


class EventSerializer(serializers.ModelSerializer):

    support_contact = SupportTeam
    event_status = Contract

    class Meta:
        model = Event
        fields = '__all__'

    def log(self, log_error):
        raise serializers.ValidationError({'Exception': str(log_error)})


class EventDetailSerializer(serializers.ModelSerializer):

    support_contact = SupportTeamDetailSerializer()
    event_status = ContractDetailSerializer()
    
    class Meta:
        model = Event
        fields = '__all__'
