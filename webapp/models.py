from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

User = get_user_model()

# Create your models here.
class users(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    password = models.CharField(max_length=50)

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = users.objects.create(password=kwargs['instance'])

post_save.connect(create_profile,sender=User)
