from django.db import models

class Genre(models.Model):
    genre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.genre

class Artist(models.Model):
    artist = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.artist

class Movie(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    release_year = models.IntegerField()
    movie_art =  models.ImageField(upload_to='')
    
    def __str__(self) -> str:
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class AboutContent(models.Model):
    description = models.CharField(max_length=1000)
    about_paragraph = models.TextField()
    mission = models.CharField(max_length=500)

    def __str__(self):
        return f"About Content - {self.id}"
