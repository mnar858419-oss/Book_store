from django.urls import path
from book.views import (
    home,
    index,
    book_detail,
    create_book,
    create_category,
    create_author,
    edit_book,
    delete_book,
    archive_book,
    add_reply,

)


urlpatterns = [
    path("", home, name="home"),
    path("index/", index, name="index"),
    path("details/<str:id>/", book_detail, name="book_detail"),
    path("book/new/", create_book, name="new_book"),
    path("category/new/", create_category, name="new_category"),
    path("author/new/", create_author, name="new_author"),
    path("book/edit/<str:id>/", edit_book, name="edit_book"),
    path("book/delete/<str:id>/", delete_book, name="delete_book"),
    path("book/archive/<str:id>/", archive_book, name="archive_book"),
    path('reply/<int:review_id>/', add_reply, name='add_reply'),
]
