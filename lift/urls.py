from django.urls import path
from .views import create_lift, list_lift, move_lift, remove_lift

urlpatterns = [
    path('', list_lift),
    path('create/', create_lift),
    path('move/', move_lift),
    path('remove/', remove_lift),
]