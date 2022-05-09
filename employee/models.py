from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    age=models.IntegerField()
    department=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.email