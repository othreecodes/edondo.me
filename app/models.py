from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)


class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    comment = models.TextField()


