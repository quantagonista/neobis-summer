from django.db import models


# Create your models here.
CONTACT_TYPES = (
    (),
    (),
    (),
)


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    img_path = models.URLField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL)


class Category(models.Model):
    name = models.CharField(max_length=30)


class Branch(models.Model):
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    altitude = models.CharField(max_length=30)
    longtitude = models.CharField(max_length=30)


class Contact(models.Model):
    type = models.IntegerField(choices=CONTACT_TYPES)
    value = models.CharField(max_length=30)


class Service(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2,default=100.00)
    description = models.CharField(max_length=100)


class Image(models.Model):
    is_logo = models.BooleanField(default=False)