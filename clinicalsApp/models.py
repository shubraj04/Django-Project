from django.db import models

# Create your models here.
class Patient(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    age = models.IntegerField()

class clinicalData(models.Model):
    COMPONENT_NAME = [('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    compponentName = models.CharField(choices=COMPONENT_NAME, max_length=100)
    measuredValue = models.CharField(max_length=50)
    measureDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)