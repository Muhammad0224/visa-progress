from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'visit/main.html', {'title': 'Visa Progress'})

def elevator(request):
    return render(request, 'visit/elevator.html', {'title': 'Visa Progress'})

def login(request):
    return render(request, 'visit/login.html', {'title': 'Visa Progress'})

def form(request):
    return render(request, 'visit/form.html', {'title': 'Visa Progress'})
