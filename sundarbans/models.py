from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class WildLife(models.Model):
    w_id = models.CharField(primary_key=True, max_length=254)
    w_name = models.CharField(max_length=254)
    w_type = models.CharField(blank=True, null=True, max_length=254)
    w_pic = models.ImageField(blank=True, null=True)


class Guide(models.Model):
    g_id = models.CharField(primary_key=True, max_length=254)
    g_name = models.CharField(max_length=254)
    g_contact = models.CharField(max_length=254)
    g_email = models.EmailField()
    g_rating = models.IntegerField(null=True, blank=True)


class Spot(models.Model):
    s_id = models.CharField(primary_key=True, max_length=254)
    s_name = models.CharField(max_length=254)
    s_description = models.TextField(null=True, blank=True)
    s_pic = models.ImageField(blank=True, null=True)


class Booking(models.Model):
    choice = (('Primary', 'Primary'), ('Standard', 'Standard'), ('Combo', 'Combo'))
    package = models.CharField(max_length=254, choices=choice)
    name = models.CharField(max_length=254)
    country = CountryField()
    email = models.EmailField()
    phone = models.CharField(max_length=254)
    start_date = models.DateField()
    end_date = models.DateField()
