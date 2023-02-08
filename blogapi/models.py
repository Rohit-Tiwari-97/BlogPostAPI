from django.db import models

class BlogModel(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

