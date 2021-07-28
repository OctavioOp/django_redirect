from django.shortcuts import redirect, render, HttpResponse
from django.http import JsonResponse
from time import localtime, strftime
from datetime import date, datetime

# Create your views here.


def root(request):
    return redirect('/blogs')


def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")


def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")


def create(request):
    return redirect('/')


def show(request, val):
    return HttpResponse(f'placeholder para mostrar el blog numero {val}')


def edit(request, val):
    return HttpResponse(f'placeholder para editar el blog {val} con un método llamado edit')


def destroy(request):
    return redirect('/')


def json(request):
    return JsonResponse({
        'name': 'Octavio',
        'something': 6
    })


def home(request):
    context = {
        "fotos": [
            'https://indiehoy.com/wp-content/uploads/2020/11/rammstein-1200x675.jpg',
            'https://indiehoy.com/wp-content/uploads/2020/09/slipknot.jpg',
            'https://acordesweb.com/img/eisbrecher-27d56532e56cdd929f4c0cf78502f820.jpg',
            'https://summainferno.com/wp-content/uploads/2019/09/ghost.jpg'
        ]
    }
    return render(request, 'home.html', context)


def timez(request):
    mydate = datetime.now()
    mydate.strftime("%Y")
    

    context = {
        "day": strftime("%d", localtime()),
        "year": mydate.strftime("%Y"),
        "month": mydate.strftime("%B"),
        "hour": strftime("%H:%M %p", localtime())
    }

    return render(request, 'timezone.html',  context)
