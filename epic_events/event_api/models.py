from datetime import datetime
from django.db import models
from django.conf import settings

# Create your models here.
class SalesTeam(models.Model):

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)


class ManageTeam(models.Model):

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)


class SupportTeam(models.Model):

    user = models.ForeignKey(to=ManageTeam, on_delete=models.CASCADE, unique=True)


class Client(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=SalesTeam, on_delete=models.CASCADE)


class Contract(models.Model):
    
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    payement_due = models.DateTimeField()


class Event(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=SupportTeam, on_delete=models.CASCADE)
    event_status = models.ForeignKey(to=Contract, on_delete=models.CASCADE)
    attendees = models.IntegerField()
    event_dates = models.DateTimeField()
    notes = models.TextField()