from django.db import models
from django.utils import timezone

class Blogs(models.Model):
    class status(models.TextChoices):
        DRAFT="DR","Draft"
        PUBLISHED="PB","published"
    blog_title=models.CharField(max_length=100)
    blog_description=models.TextField()
    slug=models.SlugField(unique=True,max_length=250)
    publish=models.DateTimeField(default=timezone.now)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    Status=models.CharField(max_length=10,choices=status,default=status.DRAFT)

    class Meta():
        ordering=['-publish']
        indexes=[models.Index(fields=["-publish"])]
    def __str__(self):
        return self.blog_title