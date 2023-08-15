from django.contrib import admin

# Register your models here.
from .models import Category, Booking, MenuItem




admin.site.register(Category)
admin.site.register(Booking)
admin.site.register(MenuItem)