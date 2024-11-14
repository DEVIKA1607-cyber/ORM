from django.db import models
from django.contrib import admin
class bankloan(models.Model):
    Name=models.CharField(max_length=50)
    Accno=models.IntegerField(primary_key="accno")
    Amount=models.IntegerField()
    Interest=models.FloatField()
    Startdate=models.DateField()
    Phoneeno=models.IntegerField()
    Email=models.EmailField()
    Enddate=models.DateField()

class bankloanAdmin(admin.ModelAdmin):
    list_display=('Name','Accno','Amount','Interest','Startdate','Enddate','Email')
