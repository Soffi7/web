from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from .models import Student
from .forms import GroupForm
from .forms import StudentForm

# Create your views here.
def index_view(request):
    return render(request, 'journal/index.html')

def contacts_view(request):
    return render(request, 'journal/contacts.html')

def about_view(request):
    return render(request, 'journal/about.html')

def students_view(request):
    all_students = Student.objects.all()
    context = {
        'page_title': 'Список студентов',
        'students_list': all_students,
    }
    return render(request, 'journal/students.html', context)

def groups_view(request):
   all_groups = Group.objects.all
   context = {
        'page_title': 'Список учебных групп',
        'groups_list': all_groups,
    }
   return render(request, 'journal/groups.html', context)

def group_detail_view(request, group_id):
    group = Group.objects.get(pk=group_id)
    students_in_group = group.students.all()
    context = {
        'group': group,
        'students': students_in_group,
    }
    return render(request, 'journal/group_detail.html', context)

def student_detail_view(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {
        'student': student
    }
    return render(request, 'journal/student_detail.html', context)

def group_add_view(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('groups')
    else:
        form = GroupForm()

    context = {
        'form': form
    }
    return render(request, 'journal/group_form.html', context)

def student_add_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()

    context = {
        'form': form
    }
    return render(request, 'journal/student_form.html', context)

def group_edit_view(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm(instance=group)

    context = {
        'form': form,
        'group': group,
    }
    return render(request, 'journal/group_form.html', context)

def student_edit_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'journal/student_form.html', context)

def group_delete_view(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return redirect('groups')

    context = {
        'group': group
    }
    return render(request, 'journal/group_delete_confirm.html', context)

def student_delete_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('students')

    context = {
        'student': student
    }
    return render(request, 'journal/student_delete_confirm.html', context)