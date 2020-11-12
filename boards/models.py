from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from account.models import User
from django.urls import reverse


class Post(models.Model):
   message = models.TextField(verbose_name='', default='', blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   created_at = models.DateTimeField(('created_at'), default=timezone.now)

   def __str__(self):
        return self.message

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(('name'), max_length=150, blank=True)
    text = models.TextField(verbose_name='', default='', blank=True)
    created_at = models.DateTimeField(('created_at'), default=timezone.now)

    def __str__(self):
        return self.text
