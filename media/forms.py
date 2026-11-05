from django import forms
from .models import Movie, Anime, Series

class BaseMediaForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'slug', 'status', 'year', 'genre', 'poster', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control bg-dark text-light border-secondary'}),
            'slug': forms.TextInput(attrs={'class': 'form-control bg-dark text-light border-secondary'}),
            'status': forms.Select(attrs={'class': 'form-select bg-dark text-light border-secondary'}),
            'year': forms.NumberInput(attrs={'class': 'form-control bg-dark text-light border-secondary'}),
            'genre': forms.SelectMultiple(attrs={'class': 'form-select bg-dark text-light border-secondary'}),
            'description': forms.Textarea(attrs={'class': 'form-control bg-dark text-light border-secondary', 'rows': 4}),
        }

    class Movie(forms.ModelForm):
        class Meta:
            model = Movie

    class Series(forms.ModelForm):
        class Meta:
            model = Series

    class Anime(forms.ModelForm):
        class Meta:
            model = Anime