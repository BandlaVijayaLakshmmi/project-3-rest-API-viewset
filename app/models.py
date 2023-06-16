from django.db import models

# Create your models here.
class Product_category(models.Model):
    category_name=models.CharField(max_length=100)
    category_id=models.PositiveIntegerField()
    def __str__(self):
        return self.category_name
class Product(models.Model):
    category_name=models.ForeignKey(Product_category,on_delete=models.CASCADE)
    Pname=models.CharField(max_length=100)
    Pid=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    data=models.DateField()
    def __str__(self):
        return self.Pname