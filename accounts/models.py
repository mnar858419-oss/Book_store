from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name="تلفن")
    address = models.CharField(max_length=255, verbose_name="آدرس")
    profile_pic = models.ImageField(
        upload_to="profile_picutures",
        default="pofile_pictures/default.jpg",
        verbose_name="عکس پروفایل",
        null=True,
        blank=True,
    )
    bio = models.TextField("بیوگرافی")
    birthdate = models.DateField(verbose_name="تاریخ تولد ", null=True)

    # 🟢 اضافه شده
    credit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        verbose_name="اعتبار کاربر (تومان)",
    )

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.username
