from django.db import models

class District(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    numberofthana = models.IntegerField()
    thananame = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return self.name

