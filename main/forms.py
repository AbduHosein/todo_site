from django import forms
from .models import Application, Course
import datetime as dt

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    checked = forms.BooleanField(required=False)

class CreateApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateApplicationForm, self).__init__(*args, **kwargs)
    CSCI1101_01 = 'CS1 Section 1'
    CSCI1101_02 ='CS1 Section 2'
    COURSE_CHOICES = [
        (CSCI1101_01, 'CS1 Section 1'),
        (CSCI1101_02, 'CS1 Section 2')
    ]

    course = forms.ChoiceField(label="Please select the course you're applying to", choices=COURSE_CHOICES)
    taken_prev = forms.ChoiceField(label='Have you taken this course before?', choices= (('yes', 'Yes'), ('no', 'No')))
    prev_desc = forms.CharField(
        label='Please state the professor and the semester you took this course. Otherwise N/A',
        widget=forms.Textarea,
        )
    resume = forms.FileField(label='Upload resume')
    coverl_desc = forms.CharField(
        label='Use this space to write a cover letter/description',
        widget=forms.Textarea)
    
    class Meta:
        model = Application
        fields = ('course', 'taken_prev', 'prev_desc', 'coverl_desc')


class CreateCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateCourseForm, self).__init__(*args, **kwargs)

    HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]
    DEPT = (('CSCI', 'CSCI'),
            ('MATH', 'Mathematics'),
            ('BIOL', 'Biology'),
            ('PHYS', 'Physics'))
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
    department = forms.ChoiceField(label='Select department:', choices=DEPT)
    name = forms.CharField(label='Course Name')
    number = forms.CharField(label='Course Number (e.g. 1011)', max_length=4)
    section = forms.ChoiceField(label='Course Section', choices=HOURS)
    instructor = forms.CharField(label='Course Instructor (Last name)')
    days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=DAYS, label='Days')
    start_time = forms.TimeField(label='Start time', widget=forms.Select(choices=HOUR_CHOICES)) 
    end_time = forms.TimeField(label='End time', widget=forms.Select(choices=HOUR_CHOICES))
    disc_flag= forms.ChoiceField(label='Does the course have discussion sections? ', choices=CHOICE)
    disc_section= forms.CharField(max_length=12,required=False,label='Discussion section')  # make a new table for discussion sections?
    office_hours = forms.ChoiceField(label= 'Required office hours per week', choices=HOURS) 
    graded_hw = forms.ChoiceField(label='Homework/assignments graded in meetings?', choices=CHOICE )
    positions = forms.ChoiceField(label='Number of TAs needed', choices=HOURS)
    desc = forms.CharField(label='Description of the course', widget=forms.Textarea)

    class Meta:
        model = Course
        fields = ('department', 'name', 'number', 'section', 'instructor', 'days', 'start_time', 'end_time', 'disc_flag', 'disc_section', 'office_hours', 'graded_hw', 'positions', 'desc')