from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'genre', 'screening_date', 'theater_name', 'city', 'ticket_price', 'available_seats')
    search_fields = ('movie_title', 'genre', 'theater_name', 'city')
    list_filter = ('genre', 'screening_date', 'city')
