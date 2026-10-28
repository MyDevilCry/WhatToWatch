from typing import ClassVar

from django.contrib import admin

from main.models import Genre

from Media.models import Anime, Movie, Series


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)  # Це обов'язково для роботи autocomplete_fields!


@admin.register(Series)
class Series(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "status",
        "year",
    )
    prepopulated_fields: ClassVar[dict[str, tuple[str, ...]]] = {"slug": ("title",)}
    search_fields = ("title",)
    autocomplete_fields = ("genre",)

@admin.register(Movie)
class Movie(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "status",
        "year",
    )
    prepopulated_fields: ClassVar[dict[str, tuple[str, ...]]] = {"slug": ("title",)}
    search_fields = ("title",)
    autocomplete_fields = ("genre",)


@admin.register(Anime)
class Anime(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "status",
        "year",
    )
    prepopulated_fields: ClassVar[dict[str, tuple[str, ...]]] = {"slug": ("title",)}
    search_fields = ("title",)
    autocomplete_fields = ("genre",)
