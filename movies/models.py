from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField()
    date_created = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.date_released}'

class Character(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie.title} - {self.last_name}, {self.first_name}'