
from uuid import uuid4

from accounts.models import Student, Teacher
from django.db import models


class Course(models.Model):

    class CH(models.TextChoices):
        THREE = "3"
        FOUR = "4"

    id = models.UUIDField(primary_key=True, default=uuid4,
                          editable=False, unique=True)
    name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    ch = models.CharField(max_length=5,
                          choices=CH.choices)

    def __str__(self):
        return str(self.name)


class Classes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4,
                          editable=False, unique=True)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student, default=None)
    enrollment_start_date = models.DateField()
    enrollment_end_date = models.DateField()

    def __str__(self):
        return str(self.course)


class Attendence(models.Model):

    class Status(models.TextChoices):
        PRESENT = "P"
        ABSENT = "A"

    id = models.UUIDField(primary_key=True, default=uuid4,
                          editable=False, unique=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    _class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student, default=None)
    status = models.CharField(max_length=5,
                              choices=Status.choices, default=Status.ABSENT)

    def __str__(self):
        return str(self._class)


class TimeTable(models.Model):

    class ROOM_NO(models.TextChoices):
        ROOM_1 = "ROOM_1"
        ROOM_2 = "ROOM_2"
        ROOM_3 = "ROOM_3"
        ROOM_4 = "ROOM_4"
        NOT_ANNOUNCED = "Not Announced Yet"

    class DAYS(models.TextChoices):
        MONDAY = "MONDAY"
        TUESDAY = "TUESDAY"
        WEDNESDAY = "WEDNESDAY"
        THURSDAY = "THURSDAY"
        FRIDAY = "FRIDAY"

    days = models.CharField(max_length=50,
                            choices=DAYS.choices)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_no = models.CharField(max_length=50,
                               choices=ROOM_NO.choices, default=ROOM_NO.NOT_ANNOUNCED)
    _class = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return str(self._class) + "....." + str(self.days)
