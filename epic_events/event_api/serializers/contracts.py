from rest_framework import serializers

from event_api.models import Contract, Client, SalesTeam
from .management import UserMinimalSerializer


class ContractSerializer(serializers.ModelSerializer):

    client = Client

    class Meta:
        model = Contract
        fields = '__all__'


class ContractDetailSerializer(serializers.ModelSerializer):

    class EmbeddedClientSerializer(serializers.ModelSerializer):

        class EmbeddedSalesTeamSerializer(serializers.ModelSerializer):

            user = UserMinimalSerializer()

            class Meta:
                model = SalesTeam
                fields = '__all__'


        sales_contact = EmbeddedSalesTeamSerializer()

        class Meta:
            model = Client
            fields = ('id', 'company_name', 'sales_contact')


    client = EmbeddedClientSerializer()
    
    class Meta:
        model = Contract
        fields = '__all__'
