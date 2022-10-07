from django.contrib.auth.models import User

from rest_framework import serializers

from event_api.models import SalesTeam, Client
from .management import UserMinimalSerializer


class ClientSerializer(serializers.ModelSerializer):

    sales_contact = SalesTeam

    class Meta:
        model = Client
        fields = '__all__'


class ClientDetailSerializer(serializers.ModelSerializer):

    class EmbeddedSalesTeamSerializer(serializers.ModelSerializer):

        user = UserMinimalSerializer()

        class Meta:
            model = SalesTeam
            fields = '__all__'


    sales_contact = EmbeddedSalesTeamSerializer()

    class Meta:
        model = Client
        fields = '__all__'

