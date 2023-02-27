from django.http import JsonResponse
from .models import Lift

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
    return JsonResponse({"Moved lift": 1})

def remove_lift(request):
    lift = Lift.objects.last()
    deleted_lift = {"id": lift.id, "current_floor": lift.current_floor, "move_up": lift.move_up, "door_open": lift.door_open, "busy": lift.busy}
    if not lift.busy:
        lift.delete()
        return JsonResponse({"Removed lift": deleted_lift})
    return JsonResponse({"Error": "Cant remove a moving lift"})
