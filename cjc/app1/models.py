from django.db import models

# Create your models here.


class Employee(models.Model):
    ename= models.CharField(max_length=50)
    img = models.ImageField(upload_to='')
    resume = models.FileField(upload_to="")


    def __str__(self):
        return f"{self.ename}--{self.img}"