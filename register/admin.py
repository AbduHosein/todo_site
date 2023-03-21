from django.contrib import admin
from register.models import Student, User, Instructor, Admin
# Register your models here.
admin.site.register(Student)
admin.site.register(User)
admin.site.register(Instructor)
admin.site.register(Admin)