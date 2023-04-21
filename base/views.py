from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

# rooms=[
#     {'id':1, 'name':'Lets learn Python!'},
#     {'id':2, 'name':'Desgin!'},
#     {'id':3, 'name':'LPython'},
# ]

def home(request):
    rooms = Room.objects.all()   
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request,pk):
    room = Room.object.get(id=pk)
    for i in rooms:
        if i['id']== int(pk):
            room=i 
    context={'room': room }
    return render(request, 'base/room.html', context )