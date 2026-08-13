from django.db import models

# Create your models here.
class BillGatesBhavan(models.Model):
    department_name = models.CharField(max_length=100)
    no_of_students = models.IntegerField(null=True)
    