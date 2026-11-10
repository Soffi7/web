from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Group, Student, Grade, Teacher, Subject
from .forms import GroupForm, StudentForm, GradeForm, TeacherForm, SubjectForm


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
    all_groups = Group.objects.all()
    context = {
        'page_title': 'Список учебных групп',
        'groups_list': all_groups,
    }
    return render(request, 'journal/groups.html', context)


def student_detail_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student
    }
    return render(request, 'journal/student_detail.html', context)


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


def student_delete_view(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('students')

    context = {
        'student': student
    }
    return render(request, 'journal/student_delete_confirm.html', context)


def grade_add_view(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GradeForm()

    context = {
        'form': form,
        'page_title': 'Выставить новую оценку'
    }
    return render(request, 'journal/grade_form.html', context)


class GroupListView(ListView):
    model = Group
    template_name = 'journal/groups.html'
    context_object_name = 'groups_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('name')


class GroupDetailView(DetailView):
    model = Group
    template_name = 'journal/group_detail.html'
    context_object_name = 'group'
    pk_url_kwarg = 'group_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = Student.objects.filter(group=self.object)
        context['students'] = students
        context['student_count'] = students.count()
        context['grades'] = Grade.objects.filter(student__in=students)
        form = GradeForm()
        form.fields['student'].queryset = students
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_detail', group_id=self.object.id)
        return self.render_to_response(self.get_context_data(form=form))


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'journal/group_form.html'
    success_url = reverse_lazy('groups')

    def form_valid(self, form):
        messages.success(self.request, f"Группа '{form.instance.name}' успешно создана!")
        return super().form_valid(form)


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'journal/group_form.html'
    context_object_name = 'group'
    pk_url_kwarg = 'group_id'
    success_url = reverse_lazy('groups')

    def form_valid(self, form):
        messages.success(self.request, f"Группа '{form.instance.name}' успешно обновлена!")
        return super().form_valid(form)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'journal/group_delete_confirm.html'
    context_object_name = 'group'
    pk_url_kwarg = 'group_id'
    success_url = reverse_lazy('groups')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        group_name = self.object.name
        messages.success(self.request, f"Группа '{group_name}' успешно удалена!")
        return super().post(request, *args, **kwargs)


class StudentListView(ListView):
    model = Student
    template_name = 'journal/students.html'
    context_object_name = 'students_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('last_name')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'journal/student_detail.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group_name'] = self.object.group.name
        return context


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'journal/student_form.html'
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        messages.success(self.request, f"Студент '{form.instance.last_name} {form.instance.first_name}' успешно создан!")
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'journal/student_form.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        messages.success(self.request, f"Студент '{form.instance.last_name} {form.instance.first_name}' успешно обновлен!")
        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'journal/student_delete_confirm.html'
    context_object_name = 'student'
    pk_url_kwarg = 'student_id'
    success_url = reverse_lazy('students')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        student_name = f"{self.object.last_name} {self.object.first_name}"
        messages.success(self.request, f"Студент '{student_name}' успешно удален!")
        return super().post(request, *args, **kwargs)


class TeacherListView(ListView):
    model = Teacher
    template_name = 'journal/teacher_list.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        return Teacher.objects.order_by('last_name')


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'journal/teacher_detail.html'
    context_object_name = 'teacher'


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'journal/teacher_form.html'
    success_url = reverse_lazy('teachers')

    def form_valid(self, form):
        messages.success(self.request, f"Учитель '{form.instance.last_name}' успешно добавлен!")
        return super().form_valid(form)


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'journal/teacher_form.html'
    success_url = reverse_lazy('teachers')

    def form_valid(self, form):
        messages.success(self.request, f"Данные учителя обновлены!")
        return super().form_valid(form)


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'journal/teacher_confirm_delete.html'
    success_url = reverse_lazy('teachers')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, f"Учитель удален!")
        return super().post(request, *args, **kwargs)


class SubjectListView(ListView):
    model = Subject
    template_name = 'journal/subject_list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        return Subject.objects.order_by('title')


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'journal/subject_detail.html'
    context_object_name = 'subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers_list'] = self.object.teachers.all()
        return context


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'journal/subject_form.html'
    success_url = reverse_lazy('subjects')

    def form_valid(self, form):
        messages.success(self.request, f"Предмет '{form.instance.title}' создан!")
        return super().form_valid(form)


class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'journal/subject_form.html'
    success_url = reverse_lazy('subjects')

    def form_valid(self, form):
        messages.success(self.request, f"Предмет обновлен!")
        return super().form_valid(form)


class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = 'journal/subject_confirm_delete.html'
    success_url = reverse_lazy('subjects')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(self.request, f"Предмет удален!")
        return super().post(request, *args, **kwargs)