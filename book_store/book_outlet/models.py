from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=10)
    code = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.name}, {self.code}"
    

class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.street}, {self.postal_code}, {self.city}"
    

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField( validators = [ MinValueValidator(1) , MaxValueValidator(5) ])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True, null=False)
    published_countries = models.ManyToManyField(Country)


    def __str__(self):
        return f"{self.title} ({self.rating})"