from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movietype/', views.movietype, name='movietype'),
    path('movie/', views.movie, name='movie'),
    path('production/', views.production, name='production'),
    path('event/', views.event, name='event'),
    path('review/', views.review, name='review'),
    path('moviedetail/<int:id>', views.moviedetail, name='details'),
    path('newEvent', views.newEvent, name='newevent'),
    path('newReview', views.newReview, name='newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]