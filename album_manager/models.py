from django.db import models

# Create your models here.

class Autor(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=150, null=False)
    country = models.CharField(max_length=30, null=False)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Album (models.Model):
    album_name = models.CharField(max_length=50, null=False)
    release_year = models.DateField(null=False)
    genre = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='album-images')
    
    def __str__(self) -> str:
        return f'{self.album_name}'