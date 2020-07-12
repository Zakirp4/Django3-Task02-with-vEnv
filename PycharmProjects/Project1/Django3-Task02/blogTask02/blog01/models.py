from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    # cat = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    cat = models.CharField(max_length=50, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # author = models.CharField(max_length=50, blank=True)
    view_count = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

