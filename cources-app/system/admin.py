from django.contrib import admin

from .models import *

admin.site.register([Branch, Contact, Category, Course])
