from django.db import models

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=2048)
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return self.name
