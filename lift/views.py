from django.http import JsonResponse
from .models import Lift
import sys

# Create your views here.
def create_lift(request):
    Lift.objects.create()
    return JsonResponse({"Status": "Lift created successfully"})

def list_lift(request):
    lifts = Lift.objects.all()
    lift_object = {}
    for lift in lifts:
        lift_object[lift.id]={"id": lift.id, "current_floor": lift.current_floor, "move_up": lift.move_up, "door_open": lift.door_open, "busy": lift.busy}
    if len(lifts)==0:
        return JsonResponse({"Error": "No lifts found"})
    return JsonResponse(lift_object)

def move_lift(request):
    closest_Lift = choose_lift(5)
    return JsonResponse({"Moved lift": closest_Lift})

def remove_lift(request):
    lift = Lift.objects.last()
    deleted_lift = {"id": lift.id, "current_floor": lift.current_floor, "move_up": lift.move_up, "door_open": lift.door_open, "busy": lift.busy}
    if not lift.busy:
        lift.delete()
        return JsonResponse({"Removed lift": deleted_lift})
    return JsonResponse({"Error": "Cant remove a moving lift"})


def choose_lift(requiredFloor):
    lifts = Lift.objects.all()
    distance = abs(requiredFloor-lifts[0].current_floor)
    closest_lift = 1
    for lift in lifts:
        if abs(requiredFloor-lift.current_floor) < distance:
            distance = abs(requiredFloor-lift.current_floor)
            closest_lift = lift.id
    return closest_lift
