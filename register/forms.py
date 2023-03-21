from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from register.models import User, Student, Instructor, Admin


class StudentSignUpForm(UserCreationForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    major = forms.CharField()
    eagle_id = forms.CharField()
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    grade = forms.ChoiceField(choices=YEAR_IN_SCHOOL_CHOICES)
    
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'major', 'eagle_id', 'grade')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email')  
        user.is_student = True
        user.email = email
        user.save()
        Student.objects.create(
            user=user,
            firstname = self.cleaned_data.get('firstname'),
            lastname = self.cleaned_data.get('lastname'),
            email = email,
            major = self.cleaned_data.get('major'),
            eagle_id = self.cleaned_data.get('eagle_id'),
            grade = self.cleaned_data.get('grade'))
        return user


class InstructorSignUpForm(UserCreationForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    department = forms.CharField()
    
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'department')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email')  
        user.is_instructor = True
        user.email = email
        user.save()
        Instructor.objects.create(
            user=user,
            firstname = self.cleaned_data.get('firstname'),
            lastname = self.cleaned_data.get('lastname'),
            email = email,
            department = self.cleaned_data.get('department'))
        return user        

class AdminSignUpForm(UserCreationForm):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    department = forms.CharField()
    
    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'email', 'department')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get('email') 
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname') 
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.email = email
        user.save()
        Admin.objects.create(
            user=user,
            firstname = self.cleaned_data.get('firstname'),
            lastname = self.cleaned_data.get('lastname'),
            email = email,
            department = self.cleaned_data.get('department'))
        return user