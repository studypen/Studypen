from django.db import models
from django.contrib.auth.models import User

class Classes(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    teacher = models.ForeignKey(User,related_name='classes_teacher' , on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='classes_students')
    def __str__(self):
        return self.name


class SheduleTime(models.Model):
  class DayOfWeek(models.IntegerChoices):
    SUNDAY = 1
    MONDAY = 2
    TUSEDAY = 3
    WEDNESDAY = 4
    THURSDAY = 5
    FRIDAY = 6
    SATURDAY = 7


  day_of_week = models.IntegerField(choices = DayOfWeek.choices)
  start_time = models.TimeField(auto_now=False, auto_now_add=False)
  end_time = models.TimeField(auto_now=False, auto_now_add=False)


class ResheduleTime(models.Model):
  from_date = models.DateField()
  to_date = models.DateField()
  new_start_time = models.TimeField(auto_now=False, auto_now_add=False)
  new_end_time = models.TimeField(auto_now=False, auto_now_add=False)
  original_shedule = models.ForeignKey(SheduleTime, on_delete=models.CASCADE)