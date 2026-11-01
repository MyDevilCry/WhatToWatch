from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from config.choices import ANIME_TYPE_CHOICES
from main.models import BaseModel, MediaManager, Season


class Series(BaseModel):
    seasons = GenericRelation(Season, related_query_name='series_set')


    objects = MediaManager()

    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'

    def __str__(self):
        return f"{self.title}({self.get_status_display()})"


class Anime(BaseModel):
    anime_type = models.CharField(max_length=20, choices=ANIME_TYPE_CHOICES,default='Multi', verbose_name="Anime type")
    seasons = GenericRelation(Season, related_query_name='anime_set')
    studio = models.CharField(max_length=255, verbose_name="Studio", blank=True, null=True)

    objects = MediaManager()

    class Meta:
        verbose_name = "Anime"
        verbose_name_plural = "Anime"

    def __str__(self):
        return f"{self.title}({self.get_status_display()})"


class Movie(BaseModel):
    duration_minutes = models.PositiveIntegerField(verbose_name="Тривалість (хв)", blank=True, null=True)

    objects = MediaManager()

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        indexes = [
            models.Index(fields=["title", "year"]),
        ]

    def __str__(self):
        return f"{self.title}({self.get_status_display()})"
