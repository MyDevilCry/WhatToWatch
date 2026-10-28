from django.views.generic import TemplateView
from Media.models import Anime, Series, Movie


class Main(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Movies"] = Movie.objects.optimized().order_by("?")[:10]
        context["Series"] = Series.objects.optimized().order_by("?")[:10]
        context["Anime"] = Anime.objects.optimized().order_by("?")[:10]

        return context

