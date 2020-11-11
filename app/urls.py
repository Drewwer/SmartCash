from django.urls import path
from .views import home, profile, transferencias, contacto

urlpatterns = [
    path('', home, name="home"),
    path('profile/', profile, name="profile"),
    path('transferencias/', transferencias, name="transferencias"),
    path('contacto/', contacto, name="contacto"),
]
