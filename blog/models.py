from django.db import models

# Create your models here.
class Posts(models.Model):
	posts_image = models.ImageField(upload_to='posts_images/')
	posts_text = models.CharField(max_length=5000)
