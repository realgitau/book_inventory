from django.db import models

# Create your models here.

class Book(models.Model):
    class GenerateChoices(models.TextChoices):
        CRIME = 'crime', 'Crime'
        FANTASY = 'fantasy', 'Fantasy'
        ROMANCE = 'romance', 'Romance'
        THRILLER = 'thriller', 'Thriller'
        MYSTERY = 'mystery', 'Mystery'
        HORROR = 'horror', 'Horror'
        BIOGRAPHY = 'biography', 'Biography'
        HISTORY = 'history', 'History'
        SCIENCE = 'science', 'Science'
        ART = 'art', 'Art'
        CHILDREN = 'children', 'Children'
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=GenerateChoices.choices)

    def __str__(self):
        return self.title