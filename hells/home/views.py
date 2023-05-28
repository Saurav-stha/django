from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    content = {
        'variable' : "And this is how variable is added",
        'name' : "Saurav",
        'age' : 15
    }
    return render(request , 'index.html',content)

def about(request):
    return render(request ,'about.html')

def services(request):
    return render(request, 'services.html')

def webDev(request):
    return render(request,'webDev.html')

def appDev(request):
    return render(request,'appDev.html')

def courses(request):
    return render(request,'courses.html')

def view(request):
    return render(request,'view.html')

def edit(request):
    return render(request,'edit.html')
    
def contact(request):
    if (request.method == "POST"):
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        desc = request.POST.get("Desc")
        contact = Contact(name=name, email = email, desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"Message submitted!")

    return render(request,'contact.html')
