from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *

# Create your views here.

def home(request):
    official_face = FrontPageOffice.objects.all()
    notice_data = Notice.objects.all()

    context = {
        'official_face':official_face,
        'notice_data':notice_data,
    }
   
    return render(request, 'home.html', context)




def myclass(request):
    return render(request, 'myclass.html')


def notice(request):
    notice_data = Notice.objects.all()

    context = {
        'notice_data' : notice_data
    }

    return render(request, 'notice.html', context)


def get_notice_data(request):
    moving_data = list(Notice.objects.values('title')) 

    return JsonResponse(moving_data, safe=False)



def detail_notice(request, id):
    detail_notice_data = get_object_or_404(Notice, id=id)
    

    context = {
        'detail_notice_data' : detail_notice_data
    }

    return render(request, 'detail_notice.html', context)


def gallery(request):
    image_data = Gallery.objects.all()
    context = {
        'image_data': image_data
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

def bachelor(request):
    bachelor_data = Bachelor.objects.all()

    context = {
        'bachelor_data':bachelor_data
    }
    return render(request, 'bachelor.html', context)