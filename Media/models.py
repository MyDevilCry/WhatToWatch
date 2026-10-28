from django.db import models

from main.models import BaseModel, MediaManager


class Series(BaseModel):
    episodes_count = models.PositiveIntegerField(verbose_name="Кількість серій", blank=True, null=True)

    objects = MediaManager()

    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'

    def __str__(self):
        return f"{self.title}({self.get_status_display()})"


class Anime(BaseModel):
    episodes_count = models.PositiveIntegerField(verbose_name="Кількість серій",blank=True,null=True)
    studio = models.CharField(max_length=255, verbose_name="Студія", blank=True, null=True)

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
