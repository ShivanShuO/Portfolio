from django.urls import path
from . import views

app_name = 'file'

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.index, name='about'),
    path('projects/',views.proj, name='proj'),
    path('projects/<prj_id>[0-9]+/',views.pro_detail, name='detail'),
]