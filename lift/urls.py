from django.urls import path
from .views import create_lift, list_lift, move_lift, mark_ooo, history_per_lift, toggle_door

urlpatterns = [
    path('', list_lift),
    path('create/', create_lift),
    path('move/', move_lift),
    path('ooo/', mark_ooo),
    path('history/', history_per_lift),
    path('door/', toggle_door),
]
