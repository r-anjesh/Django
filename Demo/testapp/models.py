from django.db import models

# Create your models here.

class employee(models.Model):
    emp_name = models.CharField(max_length=20)
    login_time = models.TimeField(max_length=10)
    logout_time = models.TimeField(max_length=10)

    def __str__(self):
        return self.emp_name
    
