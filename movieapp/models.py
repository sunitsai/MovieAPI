from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=300)
    released = models.DateField(null=True)
    rated = models.CharField(max_length=50)
    genre = models.CharField(max_length=200)
    imdbid = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    