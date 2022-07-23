"""bmproduction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from appoint.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage, name="home"),
    path('services/', Services, name="services"),
    path('gallery/', Gallery, name="gallery"),
    path('about/', About, name="about"),
    path('contact/', Contact, name="contact"),
    path('package/<str:pk>/', Packages, name="packages"),
    path('appointment/date_and_time/<str:pk>/', DateTimeSelection, name="date_time"),
    path('appointment/', MakeAppointment, name="user-info"),
    path('appointment/confirm', Confirm, name="confirm"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
