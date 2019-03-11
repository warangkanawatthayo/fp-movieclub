from django.test import TestCase
from .models import MovieType, Movie, Production, MovieReview, Event
from .forms import EventForm, ReviewForm
from django.urls import reverse

# test MovieType class
class MovieTypeTest(TestCase):
    def test_stringOutput(self):
        movietype=MovieType(typename='Comedy')
        self.assertEqual(str(movietype), movietype.typename)
    def test_tablename(self):
        self.assertEqual(str(MovieType._meta.db_table), 'movietype')
 
# test Production class
class ProductionTest(TestCase):
    def test_stringOutput(self):
        production=Production(producername='Craymer')
        self.assertEqual(str(production), production.producername)
    def test_tablename(self):
        self.assertEqual(str(Production._meta.db_table), 'production')
   
# test Event class
class MovieTest(TestCase):
    def test_stringOutput(self):
        movie=Movie(moviename='Mamma Mia')
        self.assertEqual(str(movie), movie.moviename)
    def test_tablename(self):
        self.assertEqual(str(Movie._meta.db_table), 'movie')

# test index view
class TestIndexView(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'movieapp/index.html')
 
# test event view
class TestEventView(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/movieapp/event')
        self.assertEqual(response.status_code, 200)
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('event'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('event'))
        self.assertTemplateUsed(response, 'movieapp/event.html')

# test add event form
class New_Event_Form_Test(TestCase):
    def test_eventForm_is_valid(self):
        form = EventForm(data={'eventtitle': "academy awards", 'eventlocation': "theatre", 'eventdate': "2019-02-24", 'eventdescription':"a perfect event" })
        self.assertTrue(form.is_valid())
    def test_eventForm_invalid(self):
        form = EventForm(data={'eventtitle': "academy awards", 'eventlocation': "theatre", 'eventdate': "2019-02-24", 'eventdescription':"a perfect event" })
        self.assertFalse(form.is_valid())
