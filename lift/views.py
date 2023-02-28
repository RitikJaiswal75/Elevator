from django.http import JsonResponse
from .models import Lift, Requests_Per_Lift

# Create your views here.
def create_lift(request):
    try:
        count = int(request.GET.get('count'))
    except:
        count = 0
    for i in range(count):
        lift = Lift.objects.create()
        request_per_lift = Requests_Per_Lift(lift = lift, history="Lift created")
        request_per_lift.save()
    if count < 0:
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
            "busy": lift.busy,
            "is_OOO": lift.is_OOO,
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
    message = "Lift called on floor "+ str(called_on_floor)
    request_per_lift = Requests_Per_Lift(lift=lift, history=message)
    request_per_lift.save()
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
        "busy": lift.busy,
        "is_OOO": lift.is_OOO,
        }
    return JsonResponse({"Lift moved": new_state})

def mark_ooo(request):
    lifts = Lift.objects.all()
    try:
        lift_to_mark = int(request.GET.get("lift"))-1
    except:
        lift_to_mark = -1
    if lift_to_mark>=0 and lift_to_mark<len(lifts):
        message = "Marked the lift OOO"
        lifts[lift_to_mark].is_OOO=not lifts[lift_to_mark].is_OOO
        lifts[lift_to_mark].save()
        if(lifts[lift_to_mark].is_OOO):
            message="Lift marked OOO"
        else:
            message = "Lift marked active"
        requests_Per_Lift = Requests_Per_Lift(lift = lifts[lift_to_mark], history = message)
        requests_Per_Lift.save()
    else:
        message = "Lift does not exist"
    return JsonResponse({"message": message })

def history_per_lift(request):
    try:
        lift_number = int(request.GET.get("lift")) - 1
    except:
        lift_number = 0
    lifts = Lift.objects.all()
    if lift_number>=0 and lift_number<len(lifts):
        history = Requests_Per_Lift.objects.filter(lift = lifts[lift_number])
        lift_history = []
        for _ in history:
            lift_history.append(_.history)
        return JsonResponse({
            "Lift id": lifts[lift_number].id,
            "history": lift_history,
            })
    else:
        return JsonResponse({"Message": "Lift not found"})

def toggle_door(request):
    try:
        lift_number = int(request.GET.get("lift")) - 1
    except:
        lift_number = 0
    lift = Lift.objects.all()[lift_number]
    if lift.is_OOO:
        return JsonResponse({"Error": "The lift is out of order or in maintanance"})
    lift.door_open = not lift.door_open
    lift.save()
    if(lift.door_open):
        message="Lift door opened"
    else:
        message = "Lift door closed"
    requests_Per_Lift = Requests_Per_Lift(lift=lift, history = message)
    requests_Per_Lift.save()
    return JsonResponse({
        "id": lift.id, 
        "current_floor": lift.current_floor, 
        "move_up": lift.move_up, 
        "door_open": lift.door_open, 
        "busy": lift.busy,
        "is_OOO": lift.is_OOO,
        })
    

def choose_lift(requiredFloor):
    lifts = Lift.objects.all()
    distance = 50000
    closest_lift = 1
    for lift in lifts:
        if lift.is_OOO:
            continue
        else:
            if abs(requiredFloor-lift.current_floor) < distance:
                distance = abs(requiredFloor-lift.current_floor)
                closest_lift = lift.id
    return closest_lift
