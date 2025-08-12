from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(max_length=6)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.no_of_guests} guests at {self.booking_date}"
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(max_length=5)

    def __str__(self):
        return f"{self.item_name} - ${self.price}"