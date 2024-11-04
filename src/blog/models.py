from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True)
    content = models.TextField()
    description = models.TextField()