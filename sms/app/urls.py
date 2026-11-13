from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about,name='about'),
    path('services/', views.services, name='services'),
    path('students/', views.students, name='view_students'),
    path('contacts/', views.contacts, name='contacts'),
    path('students/<str:name>/',views.get_student),
    path('add/',views.add_student),
]