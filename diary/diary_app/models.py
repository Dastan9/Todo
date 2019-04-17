from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    text = models.TextField()
    complete = models.BooleanField(default=False)
    pub_date = models.DateField()

   
    def __str__(self):
        return self.text

# Create your models here.
