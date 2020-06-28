from django.db import models

class StudentList(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    roll = models.IntegerField()
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.name

