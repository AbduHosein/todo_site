from django import forms
from .models import Application, Course

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
    # resume upload
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
    
    name = forms.CharField(label='Course Name')
    number = forms.CharField(label='Course Number')
    section = forms.CharField(label='Course Section')

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

    days = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=DAYS, label='Days')
    start_time = forms.TimeField(label='Start Time')
    end_time = forms.TimeField(label='End Time')
    disc_flag = forms.ChoiceField(label='Does the course have discussion sections? ', choices=CHOICE)
    disc_section = forms.CharField(label='Please enter discussion section for this course', required=False)
    office_hours = forms.ChoiceField(label= 'Required office hours per week', choices=HOURS)
    graded_hw = forms.ChoiceField(label='Homework/assignments graded in meetings?', choices=CHOICE )
    positions = forms.ChoiceField(label='Number of TAs needed', choices=HOURS)
    desc = forms.CharField(label='Description of the course', widget=forms.Textarea)
    
    class Meta:
        model = Course
        fields = ('name', 'number', 'section', 'days', 'start_time', 'end_time', 'disc_flag', 'disc_section', 'office_hours', 'graded_hw', 'positions', 'desc')
    
