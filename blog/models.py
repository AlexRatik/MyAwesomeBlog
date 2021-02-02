from django.db import models
from datetime import datetime, date

# Create your models here.

class Post(models.Model):
	post_h = models.CharField(max_length=44)
	date_of_posts = models.DateField(auto_now_add=False, auto_now=False, blank=True)
	text_of_posr = models.CharField(max_length=2000)
	post_image = models.ImageField(upload_to='post_image/')

