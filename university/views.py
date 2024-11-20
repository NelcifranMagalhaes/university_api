from university.models import Estudent, Course, Matriculation
from university.serializers import EstudentSerializer, CourseSerializer, MatriculationSerializer, ListMatriculationsStudentSerializer, ListMatriculationsCourseSerializer
from rest_framework import viewsets, generics

class EstudentViewSet(viewsets.ModelViewSet):
  queryset = Estudent.objects.all()
  serializer_class = EstudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer

class MatriculationViewSet(viewsets.ModelViewSet):
    queryset = Matriculation.objects.all()
    serializer_class = MatriculationSerializer

class ListMatriculationStudent(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matriculation.objects.filter(estudent_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListMatriculationsStudentSerializer

class ListMatriculationsCourse(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matriculation.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListMatriculationsCourseSerializer