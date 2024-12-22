from django.db import models

class Services(models.Model):
    name = models.CharField(max_length =100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='services/')

class Appointment(models.Model):
    customer_name = models.CharField(max_length = 100)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    contact = models.CharField(max_length=15)

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('hair','Hair Care'),
        ('skin','Skin Care'),
        ('body','Body Care'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to = 'products/',blank=True,null=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='hair')
    available = models.BooleanField(default = True)
    shipping_options = models.TextField(default ="Standard shipping")

    def __str__(self):
        return self.name

