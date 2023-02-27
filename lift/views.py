from django.http import JsonResponse
from .models import Lift
import sys

# Create your views here.
def create_lift(request):
    try:
        count = int(request.GET.get('count'))
    except:
        count = 0
    for i in range(count):
        Lift.objects.create()
    if count == 0:
        message = "No lifts created"
    else:
        message = "Lift(s) created successfully"
    
    return JsonResponse({
        "Status": message,
        "count": count,
        })

def list_lift(request):
    lifts = Lift.objects.all()
    lift_object = {}
    for lift in lifts:
        lift_object[lift.id]={
            "id": lift.id, 
            "current_floor": lift.current_floor, 
            "move_up": lift.move_up, 
            "door_open": lift.door_open, 
            "busy": lift.busy
            }
    if len(lifts)==0:
        return JsonResponse({"Error": "No lifts found"})
    return JsonResponse(lift_object)

def move_lift(request):
    try:
        called_on_floor = int(request.GET.get('floor'))
    except:
        called_on_floor = 1
    move_lift_id = choose_lift(called_on_floor)
    lift = Lift.objects.get(id = move_lift_id)
    move_up = False
    if(lift.current_floor < called_on_floor):
        move_up= True
    lift.current_floor = called_on_floor
    lift.move_up = move_up
    lift.save()
    new_state = {
        "id": lift.id, 
        "current_floor": lift.current_floor, 
        "move_up": lift.move_up, 
        "door_open": lift.door_open, 
        "busy": lift.busy
        }
    return JsonResponse({"after": new_state})

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
