from django.shortcuts import render
from .forms import StudentCreateForm,CourseCreateForm, UserResisterForm, UserLoginForm


#package for API
from  rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer, AppUserSerializer, CourseSerializer
from .models import Student, AppUser, Course
from rest_framework.request import Request

# api view with class Based views
class StudentApiView(APIView):
    # get methods to get list of data  i.e studnets' list
    def get(self, request):
        student_list= Student.object.all()# model object
        serializer= StudentSerializer(student_list)
        

def student_index(request):
    return render(request, "students/index")

def student_create(request):
    form=StudentCreateForm()
    context={
        "form":form
    }
    return render(request, "students/create.html", context)

def student_show(request):
    return render(request, "students/show.html")

def student_edit(request):
    return  render(request,"students/edit.html")


