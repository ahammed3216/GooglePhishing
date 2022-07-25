from django.db import models

# Create your models here.
class LoginDetails(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=50)

