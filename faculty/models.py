from django.db import models

# Create your models here.

class Facultydetails(models.Model):
	firstname = models.CharField(max_length=500)
	lastname = models.CharField(max_length=500)
	courseid = models.IntegerField()
	coursedescription = models.TextField()
