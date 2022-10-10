"""epic_events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from event_api.views import RegisterView, ManageTeamView, SalesTeamView, SupportTeamView, ClientView, ContractView, EventView

router = routers.DefaultRouter()
router.register('register', RegisterView, basename='register')
router.register('manage', ManageTeamView, basename='manage')
router.register('sales', SalesTeamView, basename='sales')
router.register('support', SupportTeamView, basename='support')
router.register('client', ClientView, basename='client')
router.register('contract', ContractView, basename='contract')
router.register('event', EventView, basename='event')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('', include(router.urls))
]
