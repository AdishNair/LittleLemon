from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateField()

    class Meta:
        ordering = ['booking_date', 'id']

    def __str__(self):
        return f'{self.name} - {self.booking_date}'


# The course material uses both names; retain the alias for compatibility.
MenuItem = Menu
