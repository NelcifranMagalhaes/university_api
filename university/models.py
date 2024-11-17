from django.db import models

from django.db import models

class Estudent(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11)
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
    code = models.CharField(max_length = 10)
    description = models.CharField(max_length = 100, blank = False)
    level = models.CharField(max_length = 1, choices = LEVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.code