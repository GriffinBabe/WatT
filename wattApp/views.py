from django.shortcuts import render_to_response
from wattApp.models import *
from django.http    import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg


def aboutus(request):
    return render_to_response('aboutus.html')


def clientspace(request):
    return render_to_response('client.html')

#helooooooo

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
    plots = []

    for plant in plants: #Makes a temperature and humidity plot for every plant and adds it to the plot list
        Tmeasures = TMeasure.objects.filter(plant=plant).values_list('value') #Temperature part
        f = plt.figure()
        plt.title(plant.name+' temperature plot.')
        plt.plot(Tmeasures,'r')
        plt.xlabel('Date')
        plt.ylabel('Temperature')
        plt.legend()
        canvas = FigureCanvasAgg(f)
        plt.close()
        #TODO: Add a way to convert canvas into an image renderable by html
        plots.append(canvas)

        HMeasure = HMeasure.object.filter(plant=plant).values_list('value') #Humidity part
        g = plt.figure()
        plt.title(plant.name+' humidity plot.')
        plt.plot(HMeasure,'b')
        plt.xlabel('Date')
        plt.ylabel('Humidity')
        plt.legend()
        gcanvas = FigureCanvasAgg(g)
        plt.close()
        #TODO: Same here
        plots.append(gcanvas)


def sativa(request):
    plant = Plant.objects.filter(name="Sativa")
    mesures = TMeasure.objects.filter(plant=plant).values_list('value')
    print(mesures)
    f = plt.figure()
    plt.plot(mesures,'r')
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    plt.ylim(10,40)
    plt.legend()
    canvas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    plt.close(f)
    return response