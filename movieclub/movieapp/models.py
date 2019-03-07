from django.db import models
from django.contrib.auth.models import User

# Movie Type
class MovieType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='movietype'

# Production
class Production(models.Model):
    producername=models.CharField(max_length=255)
    directorname=models.CharField(max_length=255)
    productionlocation=models.CharField(max_length=255)
    productionurl=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.producername

    class Meta:
        db_table='production'

# Movie
class Movie(models.Model):    
    moviename=models.CharField(max_length=255)
    movietype=models.ForeignKey(MovieType, on_delete=models.DO_NOTHING)
    production=models.ForeignKey(Production, on_delete=models.DO_NOTHING)
    movieyear=models.CharField(max_length=255)
    moviebudget=models.CharField(max_length=255)
    moviedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.moviename

    class Meta:
        db_table='movie'

# Movie Review
class MovieReview(models.Model):
    reviewtitle=models.CharField(max_length=255)
    reviewdate=models.DateField()
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewrating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='moviereview'

# Movie Event
class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.CharField(max_length=255)
    eventdate=models.DateField()
    eventtime=models.TimeField()
    eventdescription=models.TextField()

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'
