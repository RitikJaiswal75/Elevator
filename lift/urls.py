from django.urls import path
from .views import create_lift, list_lift

urlpatterns = [
    path('', list_lift),
    path('create/', create_lift),
]