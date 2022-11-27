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

def primeNumbers(request):
    inputNumber = 100
    primeNumbers = []

    for number in range(2, (inputNumber+1)):
        flag = False
        print('Main Number')
        print(number)
        for chkNumber in range((number-1), 1, -1):
            print('CHK Number')
            print(chkNumber)
            if number % chkNumber == 0:
                print('true')
                flag = True
                break
        
        if flag == False:
            primeNumbers.append(number)
        

    return HttpResponse(' '.join(str(e) for e in primeNumbers))

