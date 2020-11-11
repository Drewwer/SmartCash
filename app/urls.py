from django.urls import path
from .views import home, profile, transferencias

urlpatterns = [
    path('', home, name="home"),
    path('profile/', profile, name="profile"),
    path('transferencias/', transferencias, name="transferencias"),
]
