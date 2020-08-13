from django.contrib import admin
from first.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno','marks','addr']

admin.site.register(Student,StudentAdmin)
