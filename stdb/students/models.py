from django.db import models
class Students(models.Model):
  
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  enrollmentno = models.CharField(primary_key=True,max_length=255)
  specialization = models.CharField(max_length=255)
# Create your models here.
