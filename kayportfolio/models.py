from django.db import models

# Create your models here.
class Contact(models.Model):
    mobile=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
   
    
