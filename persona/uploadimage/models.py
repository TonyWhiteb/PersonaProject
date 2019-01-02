

# Create your models here.
from django.db import models # import the Django models namespace


# Our main model: Uploaded Image
class UploadedImage(models.Model):
    image = models.ImageField("Uploaded image") # stores the filename of an uploaded image