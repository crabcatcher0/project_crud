from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from app_crud.models import *
from .forms import *


# Create your views here.


def admin_login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = authenticate(request, username=username, password=password)

            if user_obj and user_obj.is_superuser:
             login(request, user_obj)
             return redirect('dashboard/')
            
            messages.info(request, 'Invalid username/password')

        return render(request, 'login.html', {'error_message': messages.get_messages(request)})
    
    except Exception as e:
        print(e)
        return render(request, 'error.html', {'error_message': str(e)})




def admin_dashboard(request):
    return render(request, 'dashboard.html')


def admission_number(request):
    data = AdmissionNumber.objects.all()
    form = AdmissionNumberForm()

    if request.method == 'POST':
        form = AdmissionNumberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admission_number')
        
    context = {
        'data': data,
        'form': form,
        'current_page': 'Admission Numbers'
    }
    return render(request, 'admission_number.html', context)


def delete_admission_number(request, id):
    data = get_object_or_404(AdmissionNumber, pk=id)
    data.delete()

    messages.success(request, 'Admission number deleted successfully.')

    return redirect('admission_number')


def delete_confirm(request, id):
    data = get_object_or_404(AdmissionNumber, pk=id)

    context = {
        'data': data,
        'current_page':'Confirm Delete'
        }
    return render(request, 'confirmation_page.html', context)
    

def contact_numbers(request):
    phone_data = ContactNumber.objects.all()
    form = ContactNumberForm()

    if request.method == 'POST':
        form = ContactNumberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Number Added Successfuly.')

            return redirect('contact_numbers')
        
    context={
        'phone_data' : phone_data,
        'form' : form,
        'current_page' : 'Contact Numbers'
    }
    return render(request, 'contact_numbers.html', context)

    