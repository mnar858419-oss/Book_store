from django.db import models
from django.conf import settings
import uuid


class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField("نام خانوادگی", max_length=50)
    birthdate = models.DateField(null=True, verbose_name="تاریخ تولد")
    biography = models.TextField(null=True, blank=True, verbose_name="زندگی‌نامه")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "نویسنده"
        verbose_name_plural = "نویسنده‌"


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("عنوان" , max_length=50)
    author = models.ForeignKey(
        "Author", on_delete=models.SET_NULL, null=True, verbose_name="نویسنده"
    )
    category = models.ForeignKey( "Category" , on_delete=models.PROTECT , verbose_name='دسته بندی')
    published_day = models.DateField("تاریخ انتشار")
    pages = models.PositiveSmallIntegerField("تعداد صفحه" , default=0)
    summary = models.TextField("خلاصه")
    cover = models.ImageField("عکس جلد" , upload_to="covers", default="covers/default.jpeg")
    created_at = models.DateTimeField("تاریخ ساخت" , auto_now_add=True)
    updated_at = models.DateTimeField("تاریخ ویرایش" , auto_now=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}-{self.author}"


# class Review(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="user_reviews",
#     )
#     book = models.ForeignKey(
#         "Book", on_delete=models.CASCADE, related_name="book_reviews"
#     )
class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='reviews', verbose_name='کتاب')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_reviews", verbose_name='کاربر')

    RATING_CHOICES = (
        (1, '۱ ستاره'),
        (2, '۲ ستاره'),
        (3, '۳ ستاره'),
        (4, '۴ ستاره'),
        (5, '۵ ستاره'),
    )

    rating = models.IntegerField(choices=RATING_CHOICES, default=5, verbose_name='امتیاز')
    comment = models.TextField(verbose_name='نظر', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ')

    class Meta:
        verbose_name = "نظرسنجی"
        verbose_name_plural = "نظرسنجی‌ها"
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.book.title} ({self.rating} stars)'


class Reply(models.Model):

    review = models.ForeignKey(
        'Review', 
        on_delete=models.CASCADE, 
        related_name='replies',
        verbose_name='ریپلای ها'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="user_replies",
        verbose_name='کاربر'
        
    )

    comment = models.TextField(
        verbose_name='پاسخ',
        max_length=500
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        verbose_name='تاریخ'
    )

    class Meta:
        verbose_name = 'پاسخها'
        verbose_name_plural = "پاسخها"
        ordering = ['created_at']
        
    def __str__(self):
        return f'Replied by {self.user.username} on Review ID {self.review.id}'
