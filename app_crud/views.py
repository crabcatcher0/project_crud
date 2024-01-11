from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *

# Create your views here.

def home(request):
    front_page_data = FrontPage.objects.first()
    official_face = FrontPageOffice.objects.all()


    context = {
        'front_page_data': front_page_data,
        'official_face':official_face

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

