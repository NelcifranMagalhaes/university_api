from django.db import models
from django.core.validators import MinLengthValidator

class Estudent(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11, unique=True)
    birth_date = models.DateField()
    phone = models.CharField(max_length = 14)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    LEVEL = (
        ('B','Basic'),
        ('I','Intermediary'),
        ('A','Advanced'),
    ) 
    code = models.CharField(max_length = 10, unique=True, validators=[MinLengthValidator(3)])
    description = models.CharField(max_length = 100, blank = False)
    level = models.CharField(max_length = 1, choices = LEVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.code
    
class Matriculation(models.Model):
    PERIOD = (
        ('M','Morning'),
        ('V','Evening'),
        ('N','Night'),
    )
    estudent = models.ForeignKey(Estudent,on_delete = models.CASCADE)
    course = models.ForeignKey(Course,on_delete = models.CASCADE)
    period = models.CharField(max_length = 1, choices = PERIOD, blank = False, null = False, default = 'M')