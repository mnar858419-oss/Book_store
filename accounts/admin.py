from django.contrib import admin
from django.utils.html import format_html
from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "credit_display",
        "is_staff",
        "is_superuser",
    )

    list_filter = ("is_staff", "is_superuser", "birthdate")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("-date_joined",)

    # فیلدهایی که در فرم ویرایش نمایش داده می‌شوند
    fieldsets = (
        ("اطلاعات کاربری", {
            "fields": (
                ("username", "password"),
                ("first_name", "last_name", "email"),
                ("birthdate", "phone_number"),
                "address",
                "bio",
                "profile_pic",
            )
        }),
        ("سطح دسترسی‌ها", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("اعتبار و وضعیت مالی", {
            "fields": ("credit",),
        }),
        ("زمان‌ها", {
            "fields": ("last_login", "date_joined"),
        }),
    )

    # فیلدهایی که در صفحه‌ی اضافه‌کردن کاربر نمایش داده می‌شوند
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username",
                "email",
                "password1",
                "password2",
                "first_name",
                "last_name",
                "credit",
                "is_staff",
                "is_superuser",
            ),
        }),
    )

    # نمایش اعتبار به‌صورت رنگی در لیست
    def credit_display(self, obj):
        color = "red" if obj.credit <= 0 else "green"
        return format_html('<b style="color:{};">{} تومان</b>', color, obj.credit)
    credit_display.short_description = "اعتبار"

    # فقط خواندنی بودن فیلدهای زمانی
    readonly_fields = ("last_login", "date_joined")
