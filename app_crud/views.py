from django.shortcuts import render, get_object_or_404
from .models import Notice

# Create your views here.

def home(request):
    return render(request, 'home.html')

def myclass(request):
    return render(request, 'myclass.html')


def notice(request):
    notice_data = Notice.objects.all()

    context = {
        'notice_data' : notice_data
    }

    return render(request, 'notice.html', context)


def detail_notice(request, id):
    detail_notice_data = get_object_or_404(Notice, id=id)
    print(detail_notice_data)

    context = {
        'detail_notice_data' : detail_notice_data
    }

    return render(request, 'detail_notice.html', context)