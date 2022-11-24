from django.shortcuts import render
from .models import Player
from django.http import HttpResponse, HttpResponseServerError, HttpResponseNotFound

# Create your views here.
def home(request):
    players = Player.objects.all()
    return render(request, 'player/home.html', { 'players': players })

def getPlayer(request):
    playerId = request.GET['id']

    try:
        player = Player.objects.get(id=playerId)
        return render(request, 'player/player-data.html', { 'player': player })
    except:
        return HttpResponseNotFound('City not found')

def addPlayer(request):
    return render(request, 'player/add-player.html')    

def create(request):
    if request.method == 'POST':
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        email = request.POST['email']
        dateOfBirth = request.POST['dateofbirth']
        isActive = True;
        if request.POST['isactive'] == 'false':
            isActive = False
        
        player = Player(
            first_name=firstName,
            last_name=lastName,
            email=email,
            date_of_birth=dateOfBirth,
            is_active=isActive
        )

        try:
            player.save()
            return HttpResponse('New player has been created successfully')
        except Exception as e:
            return HttpResponseServerError('Something went wrong' + e)


