from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def home(request):
    official_face = FrontPageOffice.objects.all()
    notice_data = Notice.objects.all().order_by('-created_at')
   
    context = {
        'official_face':official_face,
        'notice_data':notice_data,
    }
   
    return render(request, 'home.html', context)


def myclass(request):
    return render(request, 'myclass.html')


def notice(request):
    notice_data = Notice.objects.all().order_by('-created_at')
    paginated_data = Paginator(notice_data, 6)

    page_number = request.GET.get("page")
    page_data = paginated_data.get_page(page_number)


    context = {
        # 'notice_data' : notice_data,
        'page_data':page_data
    }

    return render(request, 'notice.html', context)




def get_latest_notice(request):
    latest_notices = Notice.objects.order_by('-created_at')[:3].values('title')

    return JsonResponse(list(latest_notices), safe=False)


def detail_notice(request, id):
    detail_notice_data = get_object_or_404(Notice, id=id)
    

    context = {
        'detail_notice_data' : detail_notice_data
    }

    return render(request, 'detail_notice.html', context)


def gallery(request):
    image_data = Gallery.objects.all()
    paginated_image = Paginator(image_data, 6)

    page_number = request.GET.get("page")
    page_data = paginated_image.get_page(page_number)

    context = {
        # 'image_data': image_data
        'page_data':page_data
    }
    return render(request, 'gallery.html', context)


def about_us(request):   
    return render(request, 'about_us.html')


def plus2(request):
    plus2_data = Plus2.objects.all()
    
    context = {
        'plus2_data':plus2_data
    }
    return render(request, '+2.html', context)


def plus2_details(request, id):
    print("Id", id)

    plus2_data_details = get_object_or_404(Plus2, id=id)


    context = {
        'plus2_data_details':plus2_data_details,
        'id':id
    }
    return render(request, '+2_details.html', context)


def bachelor(request, id=None):
    bachelor_data = Bachelor.objects.all()
    bachelor_data_details = None

    if id is not None:
        bachelor_data_details = get_object_or_404(Bachelor, id=id)
        context ={
            'bachelor_data_details': bachelor_data_details
        }
        return render(request, 'bachelor_details.html', context)
    
    context = {
        'bachelor_data': bachelor_data,
    }
    return render(request, 'bachelor.html', context)


def master_course(request, id=None):
    master_course_data = MasterProgram.objects.all()
    master_course_data_details = None

    if id is not None:
        master_course_data_details = get_object_or_404(MasterProgram, id=id)
        context = {
            'master_course_data_details':master_course_data_details
        }
        return render(request, 'master_details.html', context)
    
    context = {
        'master_course_data':master_course_data
    }
    return render(request, 'master.html', context)


def contact_us(request):
    if request.method == 'POST':
        fullName = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')

        contact_message = ContactUs(
            fullName=fullName,
            email=email,
            phone=phone,
            address=address,
            message=message
        )
        contact_message.save()

        messages.success(request, 'Your message was sent successfully.')

        return redirect(reverse('contact') + '?success= Your message was sent successfully.')
    
    return render(request, 'contact.html')


def download_all(request):
    downloadable_file_data = DownloadableFile.objects.all()

    context = {
        'downloadable_file_data':downloadable_file_data
    } 
    return render(request, 'downloads.html', context)

