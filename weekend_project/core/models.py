from django.db import models
from datetime import date
# Create your models here.

class Blog_User(models.Model):
    """Contains information relating to the blog user."""
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.username




class Blog_Posts(models.Model):
    """Will contain information relating to the post itself, including its
    content and author."""
    
    title = models.CharField(max_length=80)
    author = models.ForeignKey(Blog_User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1800, help_text="Enter your content here.")
    post_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title