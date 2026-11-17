from unittest.mock import patch

import requests
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from main.services import fetch_movie_data_from_tmdb
from media.models import Movie


class FetchMovieDataTests(TestCase):
    @patch("main.services.requests.get")
    def test_returns_overview_from_first_result(self, get):
        get.return_value.status_code = 200
        get.return_value.json.return_value = {
            "results": [{"overview": "A thief enters dreams."}]
        }
        get.return_value.raise_for_status.return_value = None

        self.assertEqual(
            fetch_movie_data_from_tmdb("Inception"),
            {"description": "A thief enters dreams."},
        )
        self.assertIn("/search/movie", get.call_args.args[0])

    @patch("main.services.requests.get")
    def test_returns_none_when_request_fails(self, get):
        get.side_effect = requests.RequestException("down")
        self.assertIsNone(fetch_movie_data_from_tmdb("Inception"))


class MovieSaveTests(TestCase):
    def _movie(self, **overrides):
        fields = {
            "title": "Inception",
            "slug": "inception",
            "year": 2010,
            "cover_image": SimpleUploadedFile("cover.jpg", b"cover", content_type="image/jpeg"),
        }
        fields.update(overrides)
        return Movie(**fields)

    @patch("media.models.fetch_movie_data_from_tmdb")
    def test_saves_movie_that_already_has_a_description(self, fetch):
        movie = self._movie(description="Already written")
        movie.save()

        fetch.assert_not_called()
        stored = Movie.objects.get(slug="inception")
        self.assertEqual(stored.description, "Already written")
        self.assertEqual(stored.title, "Inception")

    @patch("media.models.fetch_movie_data_from_tmdb", return_value={"description": "From TMDB"})
    def test_fills_missing_description_and_still_saves(self, fetch):
        movie = self._movie(description="")
        movie.save()

        fetch.assert_called_once_with("Inception")
        stored = Movie.objects.get(slug="inception")
        self.assertEqual(stored.description, "From TMDB")

    @patch("media.models.fetch_movie_data_from_tmdb", return_value=None)
    def test_saves_when_lookup_returns_nothing(self, fetch):
        movie = self._movie(slug="unknown", description="")
        movie.save()

        fetch.assert_called_once_with("Inception")
        self.assertTrue(Movie.objects.filter(slug="unknown", description="").exists())
