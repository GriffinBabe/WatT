from django.shortcuts import render_to_response, render
from wattApp.models import *
from django.http    import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
import matplotlib
matplotlib.use('Agg') #Necessary to avoid GUI conflicts between matplotlib and django
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg


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
    '''Currently displays both humidity and temperature graphs
    of each plant owned by the user registered in the session'''

    if 'user_id' not in request.session or len(User.objects.filter(user_id=request.session['user_id'])) == 0:#If session has expired, send to login
        return HttpResponseRedirect('/')

    user_id=request.session['user_id']
    user=User.objects.get(user_id=user_id)
    plants=Plant.objects.filter(owner=user)
    plant_plot_names = []

    Tmeasures = User_Measure.objects.filter(user=user).values_list('temperature')  # Room part
    HRoomMeasures = User_Measure.objects.filter(user=user).values_list('humidity')
    f = plt.figure()
    plt.title('Temperature (red) & Humidity (blue) Evolution')
    plt.plot(Tmeasures, 'r')
    plt.plot(HRoomMeasures,'b')
    plt.xlabel('Date')
    plt.ylabel('Temperature & Humidity')
    plt.legend()
    canvas = FigureCanvasAgg(f)
    title = user.user_id + '_Temperature.png'
    plt.savefig('wattApp/static/' + title)  # We save the plot in the static directory
    room_plot_name = title
    plt.close()

    hmes=[]

    for plant in plants: #Makes a temperature and humidity plot for every plant and adds it to the plot list
        HMeasures = Plant_Measure.objects.filter(plant=plant).values_list('humidity') #Humidity part
        g = plt.figure()
        plt.title(plant.name+' Humidity Evolution')
        plt.plot(HMeasures,'b')
        plt.xlabel('Date')
        plt.ylabel('Humidity')
        plt.legend()
        gcanvas = FigureCanvasAgg(g)
        title= plant.name + '_Humidity.png'
        plant_plot_names.append(title)
        plt.savefig('wattApp/static/'+title)
        plt.close()
        hmes.append(HMeasures)

    return render_to_response('sativa.html', {'list':plant_plot_names,'roomgraph':room_plot_name})