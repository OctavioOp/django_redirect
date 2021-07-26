from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def root(request):
    return redirect('/blogs')

def index(request):
    return  HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect('/')

def show(request,val):
    return HttpResponse(f'placeholder para mostrar el blog numero {val}')

def edit(request,val):
    return HttpResponse(f'placeholder para editar el blog {val} con un método llamado edit')

def delete(request,val):
    return HttpResponse(f'placeholder para borrar el blog {val} con un método llamado delete')
