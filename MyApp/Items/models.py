from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name    


class Country(models.Model):
    name = models.CharField(max_length = 255)

    class meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name    

class Company(models.Model):
    name = models.CharField(max_length = 255)
    Country_of_origin = models.ForeignKey(Country, related_name = "Companies", null = False, blank = False, on_delete = models.CASCADE)

    class meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Items(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True, null = True)
    Price = models.FloatField()
    is_sold = models.BooleanField(default = False)
    image = models.ImageField(upload_to="item_image", null = True, blank = True)
    brand = models.ForeignKey(Company, related_name = "car", on_delete = models.CASCADE)
    type = models.ForeignKey(Category, related_name = "Car", on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, related_name = "Items", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "Items"
    def __str__(self):
        return self.name    
