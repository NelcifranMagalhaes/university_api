from rest_framework import serializers
from university.models import Estudent, Course, Matriculation
from university.validators import cpf_invalid, name_invalid, phone_invalid

class EstudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudent
        fields = ['id','name','email','cpf','birth_date','phone']

    def validate(self, data):
        if cpf_invalid(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 dígitos!'})
        if name_invalid(data['name']):
            raise serializers.ValidationError({'name':'O nome só pode ter letras'})
        if phone_invalid(data['phone']):
            raise serializers.ValidationError({'phone':'O celular precisa ter 13 dígitos'})
        return data

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