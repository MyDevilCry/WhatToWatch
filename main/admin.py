from typing import ClassVar

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from main.models import Genre, Season, Country
from Media.models import Anime, Movie, Series

class SeasonInLine(GenericTabularInline):
    model = Season
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    extra = 1

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    inlines = [SeasonInLine]
    list_display = (
        "title",
        "slug",
        "year",

    )
    prepopulated_fields: ClassVar[dict[str, tuple[str, ...]]] = {"slug": ("title",)}
    search_fields = ("title",)
    autocomplete_fields = ("genre",)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "year",
    )
    prepopulated_fields: ClassVar[dict[str, tuple[str, ...]]] = {"slug": ("title",)}
    search_fields = ("title",)
    autocomplete_fields = ("genre",)


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    inlines = [SeasonInLine]
    list_display = (
        "title",
        "slug",
        "year",
    )
    prepopulated_fields: ClassVar[dict[str, tuple[str, ...]]] = {"slug": ("title",)}
    search_fields = ("title",)
    autocomplete_fields = ("genre",)

    class Media:
        js = ('admin/js/anime_toggle.js',)
