from django.contrib import admin
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.MainView.as_view(), name="main")
]