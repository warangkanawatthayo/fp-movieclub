from django.contrib import admin
from .models import MovieType, Production, Movie, MovieReview, Event

# Register your models here.
admin.site.register(MovieType)
admin.site.register(Production)
admin.site.register(Movie)
admin.site.register(MovieReview)
admin.site.register(Event)
