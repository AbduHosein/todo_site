from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from .models import ToDoList, Item, Application, Course
from .forms import CreateNewList, CreateApplicationForm, CreateCourseForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(response, id):
    todo = ToDoList.objects.get(id=id)
    
    if response.method == "POST":
        if response.POST.get("save"):
            for item in todo.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                
                item.save()
        
        elif response.POST.get("newItem"):
            txt = response.POST.get("new_text")

            if len(txt) > 2:
                todo.item_set.create(text=txt, complete=False)
            else:
                print("invalid")

    return render(response, 'main/list.html', {"todo": todo})


@login_required(login_url='/login')
def home(response):
    return render(response, 'main/home.html', {})

def apply(response, id):
    course = Course.objects.get(id=id)
    if response.method == "POST":
        form = CreateApplicationForm(response.POST, response.FILES)
        if form.is_valid():
            t = Application(course_name=course.name, user= response.user )
            resume = response.FILES['resume']
            t.resume = resume
            t.save()
            course.applications.add(t)
            course.save()
        
        return HttpResponseRedirect("/home")
    else:
        form = CreateApplicationForm()

    return render(response, 'main/create_app.html', {"form": form})


class summary(ListView):
    model = Course
    context_object_name = 'course_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        seperator = "-"
        time = str(Course.start_time) + " - " + str(Course.end_time)
        context['schedule'] = Course.days
        return context
    

def fp(response):
    return render(response, 'main/fp.html', {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {"form": form})

class CreateApplication(CreateView):
    model = Application
    form_class = CreateApplicationForm
    template_name = 'main/create_app.html'

    def get_context_data(self, **kwargs):
        kwargs['form_type'] = 'application'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return redirect('/')
    
class CreateCourse(CreateView):
    model = Course
    form_class = CreateCourseForm
    template_name = 'main/create_course.html'

    def get_context_data(self, **kwargs):
        kwargs['form_type'] = 'course'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        course_code = self.object.department + self.object.number + ': ' + self.object.name
        self.object.course_code = course_code
        self.object.save()

        return redirect('/')


