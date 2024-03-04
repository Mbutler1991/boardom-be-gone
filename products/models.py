from django.db import models
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField

class Section(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subsection(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(5.0)])
    in_stock = models.BooleanField(default=True)
    sections = models.ManyToManyField(Section)
    subsections = models.ManyToManyField(Subsection)

    def __str__(self):
        return self.name