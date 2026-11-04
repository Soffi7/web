from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('about/', views.about_view, name='about'),
    path('groups/', views.GroupListView.as_view(), name='groups'),
    path('group/<int:group_id>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('group/add/', views.GroupCreateView.as_view(), name='group_add'),
    path('group/<int:group_id>/edit/', views.GroupUpdateView.as_view(), name='group_edit'),
    path('group/<int:group_id>/delete/', views.GroupDeleteView.as_view(), name='group_delete'),
    path('students/', views.StudentListView.as_view(), name='students'),
    path('student/<int:student_id>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('student/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('student/<int:student_id>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:student_id>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('grade/add/', views.grade_add_view, name='grade_add'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('teacher/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teacher/add/', views.TeacherCreateView.as_view(), name='teacher_add'),
    path('teacher/<int:pk>/edit/', views.TeacherUpdateView.as_view(), name='teacher_edit'),
    path('teacher/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher_delete'),
    path('subjects/', views.SubjectListView.as_view(), name='subjects'),
    path('subject/<int:pk>/', views.SubjectDetailView.as_view(), name='subject_detail'),
    path('subject/add/', views.SubjectCreateView.as_view(), name='subject_add'),
    path('subject/<int:pk>/edit/', views.SubjectUpdateView.as_view(), name='subject_edit'),
    path('subject/<int:pk>/delete/', views.SubjectDeleteView.as_view(), name='subject_delete'),
]