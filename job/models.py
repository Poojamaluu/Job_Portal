from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    job_type = models.CharField(max_length=20)
    posted_by = models.ForeignKey(User,on_delete=models.CASCADE)