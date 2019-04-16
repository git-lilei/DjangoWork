from django.db import models


# Create your models here.
class ClassInfo(models.Model):
    classname = models.CharField(max_length=20)

    def __str__(self):
        return self.classname


class StudentInfo(models.Model):
    studentname = models.CharField(max_length=20)
    studentage = models.IntegerField()
    studentgender = models.BooleanField()
    classid = models.ForeignKey('ClassInfo', models.CASCADE)

    def __str__(self):
        return self.studentname

