from django.shortcuts import render
from .models import Ground, City
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest, HttpResponseNotFound

# Create your views here.
def home(request):
    grounds = Ground.objects.all()
    cities = City.objects.all()

    context = {
        'grounds': grounds,
        'cities': cities
    }
    return render(request, 'ground/home.html', context)

def addCity(request):
    return render(request, 'ground/add-city.html')  

def createCity(request):
    if request.method == 'POST':
        name = request.POST['name']
        
        city = City(
            name=name
        )

        try:
            city.save()
            return HttpResponse('New city has been created successfully')
        except Exception as e:
            return HttpResponseServerError('Something went wrong' + e)

def addGround(request):
    cities = City.objects.all()
    return render(request, 'ground/add-ground.html', { 'cities': cities})  

def createGround(request):
    if request.method == 'POST':
        name = request.POST['name']
        capacity = request.POST['capacity']
        cityId = request.POST['cityId']

        try:
            city = City.objects.get(id=cityId)
        except:
            return HttpResponseNotFound('City not found')

        ground = Ground(
            name=name,
            capacity=capacity,
            city=city
        )

        try:
            ground.save()
            return HttpResponse('New ground has been created successfully')
        except Exception as e:
            return HttpResponseServerError('Something went wrong' + e)