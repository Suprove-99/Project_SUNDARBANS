from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
