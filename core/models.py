from django.db import models

class Passenger(models.Model):
    name = models.CharField(max_length=120)
    sex = models.CharField(max_length=10)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Passenger"
        verbose_name_plural = "Passengers"