"""
Model for a Tweet.
 - name: 
 - message
 - timestamp
 methods:
    @validate_message - constrains the message before submitting to the database
"""
from django.db import models

class Tweet(models.Model):
    """
    Id field is generated on the database and it 
    has no other relevant use cases on the application
    """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Overriding parent.save. Validate before submit.
        """
        if self.validate_message():
            return super().save(*args, **kwargs)
        return None

    def validate_message(self):
        """
        validates the length of the message 
        """
        return len(self.message) < 50 and len(self.message) > 0