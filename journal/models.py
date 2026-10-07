from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'