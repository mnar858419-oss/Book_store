from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name="تلفن")
    address = models.CharField(max_length=255, verbose_name="آدرس")
    profile_pic = models.ImageField(
        upload_to="profile_picutures",
        default="pofile_pictures/default.jpg",
        verbose_name="عکس پروفایل",
    )
    bio = models.TextField("بیوگرافی")
    birthdate = models.DateField(verbose_name="تاریخ تولد ", null=True)

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"

    def __str__(self):
        return self.username
