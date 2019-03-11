from django.shortcuts import render, get_object_or_404
from .models import Movie, Production, MovieType, Event, MovieReview
from .forms import EventForm, ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'movieapp/index.html')

def movietypes (request):
    movietype_list=MovieType.objects.all()
    return render (request, 'movieapp/movietype.html', {'movietype_list':movietype_list})

def movie(request):
    movie_list = Movie.objects.all()
    return render(request, 'movieapp/movie.html', {'movie_list': movie_list})

def production(request):
    production_list = Production.objects.all()
    return render(request, 'movieapp/production.html', {'production_list': production_list})

def event(request):
    event_list = Event.objects.all()
    return render(request, 'movieapp/event.html', {'event_list': event_list})

def reviews(request):
    review_list = MovieReview.objects.all()
    return render(request, 'movieapp/review.html', {'review_list': review_list})

def moviedetail (request, id):
    detail = get_object_or_404(Movie, pk=id)
    context = {'detail': detail}
    return render (request, 'movieapp/details.html', context=context)

# form views
@login_required
def newEvent(request):
    form=EventForm
    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else:
        form=EventForm()
    return render(request, 'movieapp/newevent.html', {'form': form})

def newReview(request):
    form=ReviewForm
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ReviewForm()
    else:
        form=ReviewForm()
    return render(request, 'movieapp/newreview.html', {'form': form})

#login/logout 
def loginmessage(request):
    return render(request, 'movieapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'movieapp/logoutmessage.html')