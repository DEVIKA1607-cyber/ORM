# Ex02 Django ORM Web Application
## Date: 14/11/24

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![Alt text](<Screenshot 2024-11-16 143105.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin 
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)

models.py

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

```


## OUTPUT
![Alt text](<Screenshot (5).png>)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
