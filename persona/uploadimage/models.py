

# Create your models here.
import uuid
from django.db import models # import the Django models namespace

def rename_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

# Our main model: Uploaded Image
class UploadedImage(models.Model):
    image = models.ImageField("Uploaded image",upload_to=rename_uploaded_filename) # stores the filename of an uploaded image


