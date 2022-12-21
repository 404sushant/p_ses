from django.shortcuts import render
from .forms import StudentCreateForm,CourseCreateForm, UserResisterForm, UserLoginForm

def student_index(request):
    return render(request, "students/index")

def student_create(request):
    form=StudentCreateForm()
    context={
        "form":form
    }
    return render(request, "student/create.html", context)

def student_show(request):
    return render(request, "students/show.html")

def student_edit(request):
    return  render(request,"students/edit.html")


