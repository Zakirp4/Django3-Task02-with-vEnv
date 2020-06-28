from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return self.title
