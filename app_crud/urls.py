from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('myclass', myclass, name='myclass'),
    path('notice', notice, name='notice'),
    path('get_notice_data/', get_notice_data, name='get_notice_data'),
    path('detail_notice/<int:id>/', detail_notice, name='detail_notice'),
    path('gallery', gallery, name='gallery')
]
