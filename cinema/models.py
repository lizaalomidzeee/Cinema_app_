from django.db import models

class Movie(models.Model):
    movie_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    screening_date = models.DateField()
    theater_name = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie_title} ({self.screening_date})"
