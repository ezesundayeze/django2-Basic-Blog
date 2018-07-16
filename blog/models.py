from django.db import models
from django.utils.timezone import datetime
from django.utils.text import slugify

class users(models.Model):
    username = models.CharField(max_length=200, null=True)
    full_name = models.CharField(max_length=300, null=True)
    email = models.EmailField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.username


class post(models.Model):
    title =  models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField(max_length=200, unique = True, null=True, editable=False)
    user = models.ForeignKey('users', on_delete=models.CASCADE,null=True )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
   

class comments(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    full_name = models.CharField(max_length=200)
    content = models.TextField()