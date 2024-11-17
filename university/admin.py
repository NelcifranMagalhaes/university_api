from django.contrib import admin
from university.models import Estudent,Course

class Estudents(admin.ModelAdmin):
    list_display = ('id','name','email','cpf','birth_date','phone')
    list_display_links = ('id','name',)
    list_per_page = 20
    search_fields = ('name',)
        
admin.site.register(Estudent,Estudents)

class Courses(admin.ModelAdmin):
    list_display = ('id','code','description')
    list_display_links = ('id','code',)
    search_fields = ('code',)

admin.site.register(Course,Courses)