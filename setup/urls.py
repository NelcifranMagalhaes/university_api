
from django.contrib import admin
from django.urls import path, include
from university.views import EstudentViewSet, CourseViewSet, MatriculationViewSet, ListMatriculationsCourse, ListMatriculationStudent
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudents', EstudentViewSet, basename='Estudents')
router.register('courses', CourseViewSet, basename='courses')
router.register('matriculations', MatriculationViewSet, basename='Matriculations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/matriculations/',ListMatriculationStudent.as_view()),
    path('courses/<int:pk>/matriculations/',ListMatriculationsCourse.as_view()),
]
