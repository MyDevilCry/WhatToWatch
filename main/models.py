import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from config.choices import MEDIA_STATUS_CHOICES


class MediaQuerySet(models.QuerySet):
    def optimized(self):
        return self.prefetch_related("genre","country","favorite")

MediaManager = models.Manager.from_queryset(MediaQuerySet)

def current_year():
    return datetime.date.today().year

class Genre(models.Model):
    name = models.CharField(max_length=100,unique=True,db_index=True,verbose_name="Назва жанру")
    slug = models.SlugField(max_length=250, unique=True, db_index=True)

    def __str__(self):
        return self.name

class Country(models.Model):
        name = models.CharField(max_length=100, unique=True, verbose_name="Назва країни")
        slug = models.SlugField(max_length=100, unique=True)

        def __str__(self):
            return self.name

class BaseModel(models.Model):
    status = models.CharField(max_length=20, choices=MEDIA_STATUS_CHOICES, default='Plan',
                              verbose_name='Viewing Status')
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    title = models.CharField(
        max_length=100, verbose_name="Назва", db_index=True
    )
    genre = models.ManyToManyField(Genre, verbose_name="Жанр")
    description = models.TextField(
        max_length=5000, blank=True, null=True, verbose_name="Опис"
    )
    is_fetched = models.BooleanField(default=False)
    year = models.PositiveIntegerField(
        verbose_name="Дата виходу",
        db_index=True,
        validators=[MinValueValidator(1917), MaxValueValidator(current_year)],
    )
    favorite = models.ManyToManyField("user.User",
                                                related_name="favorite_%(class)ss",
                                                blank=True,
                                                verbose_name="В обраному у користувача")
    cover_image = models.ImageField(upload_to="media/", verbose_name="Обкладинка")

    class Meta:
        abstract = True



