from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class new(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()


class motto(models.Model):
    mottoauthor = models.CharField(max_length=30)
    content = models.TextField()