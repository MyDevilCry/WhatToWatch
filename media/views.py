from django.http import Http404
from django.views.generic import DetailView
from media.models import Anime, Movie, Series


class MediaDetailsView(DetailView):
    template_name = "media_details.html"
    context_object_name = "media"


    def get_object(self, queryset=None):
        slug = self.kwargs.get("slug")

        for model in [Anime, Movie, Series]:
            obj = model.objects.filter(slug=slug).first()
            if obj:
                return obj
        raise Http404("media not found.")







