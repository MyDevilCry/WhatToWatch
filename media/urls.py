from django.urls import path

from media import views

app_name = 'media'

urlpatterns = [
    path("details/<slug:slug>/", views.MediaDetailsView.as_view(), name="media_details"),
]