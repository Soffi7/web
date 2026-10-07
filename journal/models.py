from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Subject(models.Model):
    title = models.CharField(max_length=150)
    teachers = models.ManyToManyField(Teacher, related_name='subjects')

    def __str__(self):
        return self.title


class Grade(models.Model):
    value = models.PositiveSmallIntegerField()
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.value}'


class Attendance(models.Model):
    date = models.DateField()
    present = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='attendances')

    def __str__(self):
        return f'{self.student} - {self.subject} - {self.date}'