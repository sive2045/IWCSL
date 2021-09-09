from django.http import HttpResponse
from django.shortcuts import render

from .models import Event

def index(request):
    latest_event_list = Event.objects.order_by('-pub_date')[:5]
    context = {
        'latest_event_list' : latest_event_list,
    }
    return render(request, 'cctv/index.html')

def detail(request, event_id):
    return HttpResponse("You're looking at question %s" %event_id)