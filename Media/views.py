from django.views.generic import DetailView, ListView

from main.admin import Anime, Movie, Series


class MovieView(ListView):
    model = Movie
    template_name = "movie.html"
    context_object_name = "movie"

    def get_queryset(self):
        return Movie.objects.optimized()

class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"
    context_object_name = "movie_detail"

    def get_queryset(self):
        return Movie.objects.optimized()

class SeriesView(ListView):
    model = Series
    template_name = "series.html"
    context_object_name = "series"

    def get_queryset(self):
        return Series.objects.optimized()

class SeriesDetailView(DetailView):
    model = Series
    template_name = "series_detail.html"
    context_object_name = "series_detail"

    def get_queryset(self):
        return Series.objects.optimized()

class AnimeView(ListView):
    model = Anime
    template_name = "anime.html"
    context_object_name = "anime"

    def get_queryset(self):
        return Anime.objects.optimized()

class AnimeDetailView(DetailView):
    model = Anime
    template_name = "anime_detail.html"
    context_object_name = "anime_detail"

    def get_queryset(self):
        return Anime.objects.optimized()



