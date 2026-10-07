from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('about/', views.about_view, name='about'),
    path('students/', views.students_view, name='students'),
    path('groups/', views.groups_view, name='groups'),
]