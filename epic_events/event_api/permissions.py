from django.contrib.auth.models import User

from rest_framework.permissions import BasePermission

from .models import SalesTeam, SupportTeam, ManageTeam, Client


SAFE_METHODS = ('GET')

class IsAuthenticatedGetUser(BasePermission):
    
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and ManageTeam.objects.filter(user=request.user).exists() if request.method not in SAFE_METHODS else request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj == request.user or ManageTeam.objects.filter(user=request.user).exists() if request.method not in SAFE_METHODS else True


class IsAuthenticatedManageTeam(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and ManageTeam.objects.filter(user=request.user).exists() if request.method not in SAFE_METHODS else request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or ManageTeam.objects.filter(user=request.user).exists() if request.method not in SAFE_METHODS else True


class IsAuthenticatedGetClient(BasePermission):

    def has_permission(self, request, view):
        authenticated = request.user and request.user.is_authenticated
        if request.method not in SAFE_METHODS:
            return authenticated and SalesTeam.objects.filter(user=request.user).exists()
        else:
            return authenticated and (SalesTeam.objects.filter(user=request.user).exists() or SupportTeam.objects.filter(user=ManageTeam.objects.filter(user=request.user).exists()).exists())

    def has_object_permission(self, request, view, obj):
        return  obj.sales_contact.user == request.user if request.method not in SAFE_METHODS else True


class IsAuthenticatedGetContract(BasePermission):

    def has_permission(self, request, view):
        authenticated = request.user and request.user.is_authenticated
        if request.method not in SAFE_METHODS:
            return authenticated and SalesTeam.objects.filter(user=request.user).exists()
        else:
            return authenticated and (SalesTeam.objects.filter(user=request.user).exists() or SupportTeam.objects.filter(user=ManageTeam.objects.filter(user=request.user).exists()).exists())

    def has_object_permission(self, request, view, obj):
        return obj.client.sales_contact.user == request.user if request.method not in SAFE_METHODS else True


class IsAuthenticatedGetEvent(BasePermission):

    def has_permission(self, request, view):
        authenticated = request.user and request.user.is_authenticated
        if request.method == 'POST':
            return authenticated and SalesTeam.objects.filter(user=request.user).exists()
        else:
            return authenticated and (SalesTeam.objects.filter(user=request.user).exists() or SupportTeam.objects.filter(user=ManageTeam.objects.filter(user=request.user).exists()).exists())

    def has_object_permission(self, request, view, obj):
        return (obj.event_status.client.sales_contact.user == request.user or obj.support_contact.user.user == request.user) if request.method not in SAFE_METHODS else True
