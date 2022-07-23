from django.shortcuts import render, redirect
from bm.models import Appointment, Package, Category, Team, Gallery


from django.http import JsonResponse
import json

def Homepage(request):
    # gallery = Gallery.objects.all()
    # ctxt = {
    #     'galleries': gallery,
    # }

    return render(request, 'appoint/index.html')



def Services(request):
    category = Category.objects.all()[:10]

    ctxt = {
        'categories': category,
    }
    return render(request, 'appoint/services.html',ctxt)

def Packages(request, pk):
    category_id = Category.objects.get(id = pk)
    packages = Package.objects.filter(category=category_id)
    ctxt = {
        'packages': packages,
        'category_id':category_id,
    }
    return render(request, 'appoint/packages.html', ctxt)


def Contact(request):
    return render(request, 'appoint/contact.html')


def Gallery(request):
    # gallery = Gallery.objects.all()
    # ctxt = {
    #     'galleries': gallery,
    # }
    return render(request, 'appoint/gallery.html')

def About(request):
    teams = Team.objects.all()
    ctxt = {
        'teams': teams,
    }
    return render(request, 'appoint/about.html', ctxt)



def DateTimeSelection(request, pk):
    package = Package.objects.get(id=pk)
    category_id = package.category_id
    
    ctxt = {
        'package': package,
        'category_id':category_id,
    }
    return render(request, 'appoint/date_time.html', ctxt)


def MakeAppointment(request):
    if request.POST:
        category_id = request.POST.get('category_id')
        package_id = request.POST.get('package_id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
       
        package = Package.objects.get(id=package_id)
        category = Category.objects.get(id = category_id)
     
    ctxt = {
        'category': category,
        'package_id': package_id,
        'package':package,
        'date': date,
        'time': time,
        'phone': phone,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
       
    }
    return render(request, 'appoint/appointment.html', ctxt)


def Confirm(request):
    if request.POST:
        category_id = request.POST.get('category_id')
        package_id = request.POST.get('package_id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        package = Package.objects.get(id=package_id)
        category = Category.objects.get(id=category_id)
        appoint = []
        makeAppoint = Appointment(package=package,category=category, date=date, email=email, time=time, first_name=first_name, last_name=last_name, phone=phone)
        appoint.append(makeAppoint)
        Appointment.objects.bulk_create(appoint)
        return redirect('home')
    return render(request, 'appoint/confirmation.html')