from django.contrib import admin
from accounts.models import CustomUser
# Register your models here.


class CustomAdmin(admin.ModelAdmin):
    list_display = ["username", "is_staff", "is_superuser", "email"]
    fields = [
        ("username", "password"),
        ("first_name", "last_name", "email", "birthdate"),
    ]
    list_filter = ("is_superuser", "is_staff")
    search_fields = ["email"]


admin.site.register(CustomUser, CustomAdmin)
