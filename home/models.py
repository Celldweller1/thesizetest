from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils import timezone

# Create your models here.

class UserScan(models.Model):
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    length= models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    gender= models.CharField(max_length=255)
    age= models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    contactNumber= models.CharField(max_length=255)
    submitDate= models.DateTimeField(default=timezone.now)
    chest= models.DecimalField(max_digits=5,decimal_places=2)
    waist= models.DecimalField(max_digits=5,decimal_places=2)
    hipps= models.DecimalField(max_digits=5,decimal_places=2)
    inseem= models.DecimalField(max_digits=5,decimal_places=2)
    arm= models.DecimalField(max_digits=5,decimal_places=2)
    @classmethod
    def create(self, name, age,email,length,gender,contactNumber,chest,waist,hipps,inseem,arm):
        UserScan = self(name = name,age=age,email=email,length=length,gender=gender,contactNumber=contactNumber,chest=chest,waist=waist,hipps=hipps,inseem=inseem,arm=arm)
        # do something with the book
        return UserScan
    def __str__(self):
        return f"name={self.name}/email={self.email}/length={self.length}/gender={self.gender}/age={self.age}/contactNumber={self.contactNumber}/submitDate={self.submitDate}"
    
class SystemConfiguration(models.Model):
    key= models.CharField(max_length=255)
    value= models.CharField(max_length=255)
    @classmethod
    def create(self, key,value):
        systemConfiguration = self(key = key,value=value)
        # do something with the book
        return systemConfiguration