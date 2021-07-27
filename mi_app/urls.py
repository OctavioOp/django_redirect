from django.urls import path     
from . import views


urlpatterns = [
    path('', views.root),
    path('blogs',views.index),
    path('blogs/new',views.new),
    path('blogs/create',views.create),
    path('blogs/<int:val>',views.show),
    path('blogs/<int:val>/edit',views.edit),
    path('blogs/<int:val>/delete',views.delete),
    path('blogs/json',views.json)

]
