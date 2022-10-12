from django.db import models

class Tweet(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
