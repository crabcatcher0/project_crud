from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from app_crud.models import *
from .forms import *


# Create your views here.

#super user admin login
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



# for dashboard
def admin_dashboard(request):
    return render(request, 'dashboard.html')

# Admission number Adding
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


#deleting Admission number
def delete_admission_number(request, id):
    data = get_object_or_404(AdmissionNumber, pk=id)
    data.delete()

    messages.success(request, 'Admission number deleted successfully.')

    return redirect('admission_number')


#delete confirmation page
def delete_confirm(request, id):
    data = get_object_or_404(AdmissionNumber, pk=id)

    context = {
        'data': data,
        'current_page':'Confirm Delete'
        }
    return render(request, 'confirmation_page.html', context)
    
#adding Contact Numbers
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


#deleting contact numbers
def delete_contact_number(request, id):
    phone_data = get_object_or_404(ContactNumber, pk=id)
    phone_data.delete()

    messages.success(request, 'Contact number deleted successfully.')

    return redirect('contact_numbers')


#Confirmation page for deletion
def confirmation_page_contact(request, id):
    phone_data = get_object_or_404(ContactNumber, pk=id)

    context = {
        'phone_data':phone_data,
        'current_page':'Confirm Delete'
    }
    return render(request, 'confirmation_page_contact.html', context)


#Notices
def notice_admin(request):
    notice_data = Notice.objects.all().order_by('-created_at')
    paginated_data = Paginator(notice_data, 8)

    page_number = request.GET.get("page")
    page_data = paginated_data.get_page(page_number)

    form = NoticeForm()

    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'Notice Added Successfully.')
            return redirect('notice_admin')
    context = {
        # 'notice_data':notice_data,
        'page_data':page_data,
        'form':form,
        'current_page': 'Notice'
    }
    return render(request, 'notice_admin.html', context)


#delete Notice
def delete_notice(request, id):
    notice_data = get_object_or_404(Notice, id=id)
    notice_data.delete()

    messages.success(request, 'Notice Deleted Successfully.')

    return redirect('notice_admin')


#confirmation delete notice
def confirmation_delete_notice(request, id):
    notice_data = get_object_or_404(Notice, id=id)

    context = {
        'notice_data': notice_data,
        'current_page':'Confirm Delete'
    }
    return render(request, 'confirm_delete_notice.html', context)


#Gallery
def gallery_admin(request):
    gallery_data = Gallery.objects.all().order_by('-created_at')
    paginated_data = Paginator(gallery_data, 9)

    page_number = request.GET.get("page")
    page_data = paginated_data.get_page(page_number)

    form = GalleryForm()

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()

            messages.success(request, 'Picture Added Successfully.')
            return redirect('gallery_admin')
        
    context = {
        'page_data':page_data,
        'form':form,
        'current_page':'Gallery',
    }
    return render (request, 'gallery_admin.html', context)


#delete Image
def delete_gallery(request, id):
    image_data = get_object_or_404(Gallery, id=id)
    image_data.delete()

    messages.success(request, 'Image Deleted Successfully.')
    return redirect('gallery_admin')


#confirm Delete Image
def confirm_delete_image(request, id):
    image_data = get_object_or_404(Gallery, id=id)

    context = {
        'image_data':image_data,
        'current_page':'Confirm Delete'
    }

    return render (request, 'confirm_delete_image.html', context)