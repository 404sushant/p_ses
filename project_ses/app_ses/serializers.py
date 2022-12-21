from rest_framework import serializers
from .models import Student,Course,AppUser

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        feilds= ("first_name", "middle_name", "last_name", "email", \
            "contact", "gender", "blood_group", "academic_level", \
            "academic_status", "academic_org", "academic_score",\
            "course", "intake", "shift", "remarks")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        field= ("title","code")

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model= AppUser
        field= ("email","password")