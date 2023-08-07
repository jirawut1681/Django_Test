from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    #lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self) :
        return "ชื่อมนุษย์ = " + self.name + "อายุมนุษย์ตนนี้ = "+ str(self.age) + ", " + str(self.date)