from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Complaint(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)
