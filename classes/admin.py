from django.contrib import admin
from .models import *

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_code', 'ch', 'teacher')


class ClassesAdmin(admin.ModelAdmin):
    list_display = ('course',)


class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('date', 'start_time', 'end_time', '_class')


class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('days', 'start_time', 'end_time', 'room_no', '_class')


admin.site.register(Course, CourseAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Attendence, AttendenceAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
