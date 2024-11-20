from rest_framework import serializers
from university.models import Estudent, Course, Matriculation


class EstudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudent
        fields = ['id','name','email','cpf','birth_date','phone']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class MatriculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculation
        fields = '__all__'

class ListMatriculationsStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Matriculation
        fields = ['course','period']
    def get_period(self,obj):
        return obj.get_period_display()

class ListMatriculationsCourseSerializer(serializers.ModelSerializer):
    estudent_name = serializers.ReadOnlyField(source = 'estudent.name')
    class Meta:
        model = Matriculation
        fields = ['estudent_name']