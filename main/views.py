from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView
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
        self.object.save()

        return redirect('/')


