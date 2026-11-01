import random

from django.views.generic import TemplateView

from Media.models import Anime, Movie, Series


class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = list(Movie.objects.all())
        series = list(Series.objects.all())
        anime = list(Anime.objects.all())
        all_media = movies + series + anime
        random.shuffle(all_media)

        context["Movies"] = Movie.objects.optimized().order_by("?")[:10]
        context["Series"] = Series.objects.optimized().order_by("?")[:10]
        context["Anime"] = Anime.objects.optimized().order_by("?")[:10]
        context["random_media"] = all_media[:10]
        return context

