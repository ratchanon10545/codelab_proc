#views.py

from django.shortcuts import render, redirect

# Create your views here.
def list_view(request):
   
    actors = [{"id": '1',"name": 'Rocket falconnine'}, {"id": '2',"name": 'Dragon lowrence'}]
    
    return render(request, "main/home.html",  {'actors': actors})

def list_view2(request):
    
    return render(request, "main/ex1.html")