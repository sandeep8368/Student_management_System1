from django.db import models

# Create your models here.
class studentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    roll = models.IntegerField()
    phone = models.IntegerField()