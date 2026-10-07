from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('about/', views.about_view, name='about'),
    path('students/', views.students_view, name='students'),
    path('groups/', views.groups_view, name='groups'),
    path('group/<int:group_id>/', views.group_detail_view, name='group_detail'),
    path('student/<int:student_id>/', views.student_detail_view, name='student_detail'),
]