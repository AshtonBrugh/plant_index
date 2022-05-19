from django.shortcuts import render
from django.http import Http404

from .models import Plant

def home(request):
    plants = Plant.objects.all()
    return render(request, 'home.html', {
        'plants': plants
    })

def plant_detail(request, plant_id):
    try:
     plant = Plant.objects.get(id = plant_id)
    except Plant.DoesNotExist:
        raise Http404('Plant not found :/')
    return render(request, 'plant_detail.html', {
        'plant': plant
    })

