from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(('email address'), unique=True)
    username = models.CharField(max_length = 20,unique=False, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Student(models.Model):
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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    major = models.CharField(max_length=20)
    eagle_id = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,8}$')])
    grade = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.firstname

