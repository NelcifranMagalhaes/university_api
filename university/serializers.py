from rest_framework import serializers
from university.models import Estudent, Course


class EstudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudent
        fields = ['id','name','email','cpf','birth_date','phone']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'