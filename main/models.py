from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class Application(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    CSCI1101_01 = 'CS1 Section 1'
    CSCI1101_02 ='CS1 Section 2'
    COURSE_CHOICES = [
        (CSCI1101_01, 'CS1 Section 1'),
        (CSCI1101_02, 'CS1 Section 2')
    ]
    
    course = models.CharField(
        max_length=20,
        choices=COURSE_CHOICES,
        default=CSCI1101_01,)
    taken_prev = models.CharField(
        max_length=3,
        choices= [('yes', 'Yes'), ('no', 'No')],
        default= 'No'
    )
    prev_desc = models.CharField(max_length=40, default='test')
    #resume upload field 
    coverl_desc = models.CharField(max_length=200, default='test')
    

class Course(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    section = models.CharField(max_length=30)

    DAYS = (('M', 'Monday'),
            ('T', 'Tuesday',),
            ('W', 'Wednsday'),
            ('TH', 'Thursday'),
            ('F', 'Friday'))
    CHOICE = (('yes', 'Yes'),
                 ('no', 'No'))
    HOURS = (('1', '1'),
             ('2', '2'),
             ('3', '3'),
             ('4', '4'),
             ('5', '5'))

    days = MultiSelectField(choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    disc_flag = models.CharField(max_length=3, choices= CHOICE, default='no')
    disc_section = models.CharField(max_length=30, blank=True)
    office_hours = models.CharField(max_length=1, choices=HOURS, default='2')
    graded_hw = models.CharField(max_length=3, choices= CHOICE, default='no')
    positions = models.CharField(max_length=1, choices=HOURS, default='2')
    desc = models.CharField(max_length=200)

