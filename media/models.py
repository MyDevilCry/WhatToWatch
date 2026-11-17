from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from config.choices import ANIME_TYPE_CHOICES, MEDIA_STATUS_CHOICES
from main.models import BaseModel, MediaManager, Season
from main.services import fetch_movie_data_from_tmdb, fetch_anime_data_from_kitsu


class Series(BaseModel):
    status = models.CharField(max_length=20, choices=MEDIA_STATUS_CHOICES, default='released',
                              verbose_name='Viewing Status')
    seasons = GenericRelation(Season, related_query_name='series_set')


    objects = MediaManager()

    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'

    def __str__(self):
        return f"{self.title}({self.get_status_display()})"


class Anime(BaseModel):
    status = models.CharField(max_length=20, choices=MEDIA_STATUS_CHOICES, default='released',
                              verbose_name='Viewing Status')
    anime_type = models.CharField(max_length=20, choices=ANIME_TYPE_CHOICES,default='Multi', verbose_name="Anime type")
    seasons = GenericRelation(Season, related_query_name='anime_set')
    studio = models.CharField(max_length=255, verbose_name="Studio", blank=True, null=True)

    objects = MediaManager()

    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Anime"

    def save(self, *args, **kwargs):
        if not self.description:
            api_data = fetch_anime_data_from_kitsu(self.title)
            if api_data and api_data.get("description"):
                self.description = api_data["description"]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Movie(BaseModel):
    duration_minutes = models.PositiveIntegerField(verbose_name="Тривалість (хв)", blank=True, null=True)

    objects = MediaManager()

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        indexes = [
            models.Index(fields=["title", "year"]),
        ]


    def save(self, *args, **kwargs):
        if not self.description:
            api_data = fetch_movie_data_from_tmdb(self.title)
            if api_data and api_data.get("description"):
                self.description = api_data["description"]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
