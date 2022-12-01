from django.db import models

# Create your models here.

class Video(models.Model):
    #photo=models.ImageField(upload_to='myimage')
    videofile= models.FileField(upload_to='myimage',null='True')

    