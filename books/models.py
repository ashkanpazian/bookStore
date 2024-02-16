from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=100 , decimal_places=2)
    content = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title} by {self.author}'
