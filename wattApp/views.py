from django.shortcuts import render_to_response
from wattApp.models import *
from django.http    import HttpResponseRedirect


def aboutus(request):
    return render_to_response('aboutus.html')

def clientspace(request):
    return render_to_response('client.html')



def login(request):
    if 'user_id' in request.GET: #If the user already signed up
        user_id=request.GET['user_id']
        pwd=request.GET['pwd']
        if len(User.objects.filter(user_id=user_id)) == 1: #We check whether the user exists
            user=User.objects.get(user_id=user_id)
            if user.password == pwd:   #We match the password
                request.session['user_id']=user_id  #We record the user in the session
                return HttpResponseRedirect('home')
            else:
                error = 'Password and ID don\'t match'
                return render_to_response('login', {'error': error})
        else:
            error = 'Unknown contact'
            return render_to_response('login', {'error': error})
    else:
        request.session['user_id']=''
        return render_to_response('login')

def home(request):
    if 'user_id' not in request.session:#If session has expired, send to login
        return HttpResponseRedirect('/')

    user_id=request.session['user_id']
    user=User.objects.get(user_id=user_id)
    plants=Plant.objects.filter(owner=user)
    measures=[]
    for plant in plants:
        Hevolution=[]
        Tevolution=[]
        Hmeasures=HMeasure.objects.filter(plant=plant)
        Tmeasures=TMeasure.objects.filter(plant=plant)
        for measure in Hmeasures:
            Hevolution.append((measure.date,measure.value))
        for measure in Tmeasures:
            Tevolution.append((measure.date,measure.value))

    return render_to_response("home", {'hev':Hevolution, 'tev':Tevolution})
