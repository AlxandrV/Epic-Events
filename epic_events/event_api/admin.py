from django.contrib import admin

from .models import SalesTeam, ManageTeam, SupportTeam, Client, Contract, Event
# Register your models here.

admin.site.register([SalesTeam, ManageTeam, SupportTeam])

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'first_name', 'last_name')
    search_fields = ('company_name', 'email')


@admin.register(Contract)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_company_name', 'payement_due', 'amount', 'created_time', 'status')
    search_fields = ('client__company_name', 'client__email', 'created_time', 'amount')

    def client_company_name(self, obj):
        return obj.client.company_name


@admin.register(Event)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('event_status_client_company_name', 'event_status_client_email', 'event_dates')
    search_fields = ('event_status__client__company_name', 'event_status__client__email', 'event_dates')

    def event_status_client_company_name(self, obj):
        return obj.event_status.client.company_name
    
    def event_status_client_email(self, obj):
        return obj.event_status.client.email