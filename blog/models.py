from django.db import models

# Create your models here.
class Blog(models.Model):
	blog_image = models.ImageField(upload_to='blog_images/')
	blog_text = models.CharField(max_length=5000)
