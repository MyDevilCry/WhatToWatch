from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "email",
    )
    search_fields = ("username", "first_name", "last_name", "email")
