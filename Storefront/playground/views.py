from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from RulebaseProductionSystem import planner
from django.http import JsonResponse


# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    # pull data from db
    # transform data 
    # send email
    return render(request, 'new.html')


@api_view(['POST'])
def planner_api(request):
    plan = planner.planner(initial_state=request.data.get('initial_state'), final_state=request.data.get('final_state'),
                           positions={"type": "discrete", "values": request.data.get('position_value')},
                           constraints=request.data.get('constraints'), facts=request.data.get('general_fact'),
                           iteration_limit=1000)

    return JsonResponse({"plan": plan})
