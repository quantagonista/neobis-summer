from django.db import models

CONTACT_TYPES = (
    ('Facebook', 'Facebook'),
    ('Email', 'Email'),
    ('Phone', 'Phone'),
)


class Category(models.Model):
    name = models.CharField(max_length=30)
    img_path = models.URLField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Branch(models.Model):
    address = models.CharField(max_length=30)
    longtitude = models.CharField(max_length=30)
    altitude = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Branches'


class Contact(models.Model):
    type = models.IntegerField(choices=CONTACT_TYPES)
    value = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class Course(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    contacts = models.ManyToManyField('Contact')
    branches = models.ManyToManyField('Branch')
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    logo = models.URLField()

    class Meta:
        default_related_name = 'Courses'

    def __str__(self):
        return self.name
