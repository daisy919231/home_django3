from django.db import models

# Create your models here.
class Products(models.Model):
    title=models.CharField(max_length=100)
    image=models.TextField()
    color=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    material=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return (self.title+" "+self.brand)
