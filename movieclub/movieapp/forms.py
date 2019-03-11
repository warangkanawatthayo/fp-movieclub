from django import forms
from .models import Event, MovieReview

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model=MovieReview
        fields='__all__'