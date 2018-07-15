from django.db import models
from django.utils.timezone import datetime
from django.utils.text import slugify

class post(models.Model):
    title =  models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField(max_length=200, unique = True, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "post"