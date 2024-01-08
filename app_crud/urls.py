from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('myclass', myclass, name='myclass'),
    path('notice', notice, name='notice'),
    path('detail_notice/<int:id>/', detail_notice, name='detail_notice'),
]
