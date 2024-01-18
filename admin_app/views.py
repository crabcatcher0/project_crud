from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from app_crud.models import *


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
    context = {
        'data': data,
    }
    return render(request, 'admission_number.html', context)