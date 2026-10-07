from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'journal/index.html')

def contacts_view(request):
    return render(request, 'journal/contacts.html')

def about_view(request):
    return render(request, 'journal/about.html')

def students_view(request):
    students_list = [
        {'name': 'Иван Петров', 'status': 'отличник'},
        {'name': 'Анна Сидорова', 'status': 'хорошист'},
        {'name': 'Петр Иванов', 'status': 'отличник'},
    ]
    context = {
        'page_title': 'Список студентов',
        'students_list': students_list,
    }
    return render(request, 'journal/students.html')

def groups_view(request):
    groups_list = [
        {'id': 1, 'name': '9А Класс', 'is_active': True},
        {'id': 2, 'name': '10Б Класс (архив)', 'is_active': False},
        {'id': 3, 'name': '11В Класс', 'is_active': True},
    ]
    context = {
        'page_title': 'Список учебных групп',
        'groups_list': groups_list,
    }
    return render(request, 'journal/groups.html')