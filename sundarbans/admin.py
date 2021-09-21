from django.contrib import admin
from .models import WildLife, Guide, Spot, Booking

# Register your models here.
lst = [WildLife, Guide, Spot, Booking]
admin.site.register(lst)
