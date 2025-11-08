from doctest import REPORT_NDIFF
from math import log
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from book.models import Author, Book, Category , Review , Reply
from book.forms import CategoryForm, AuthorForm, BookForm , ReplyForm , ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


def index(request):
    return HttpResponse("Home Page")


def home(request):
    books = Book.objects.filter(is_archived=False)
    context = {"books": books}
    return render(request, "book/booklist.html", context)


def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    context = {"book": book}
    return render(request, "book/book_detail.html", context)


@login_required
def create_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "book/new_book.html", {"form": form})


@login_required
def create_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            n = data.get("name")
            d = data.get("description")
            new_category = Category.objects.create(name=n, description=d)
            print(new_category)
            return redirect("home")
    return render(request, "book/new_category.html", context={"form": form})


@login_required
def create_author(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()
            print(new_author)
            return redirect("home")
    return render(request, "book/new_author.html", {"form": form})


@login_required
def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "تغییرات با موفقیت ذخیره شد")
            return redirect("book_detail", id=id)

    return render(request, "book/edit_book.html", context={"form": form, "book": book})


@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == "POST":
        book.delete()
        return redirect("home")


@login_required
def archive_book(request, id):
    book = get_object_or_404(Book, pk=id)
    book.is_archived = True
    book.save()
    return redirect("home")

@login_required
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book=book).select_related('user').prefetch_related('replies__user')

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = book
            new_review.user = request.user
            new_review.save()
            messages.success(request, "نظر شما ثبت شد ✅")
            return redirect('book_detail', id=book.id)
    else:
        review_form = ReviewForm()

    context = {
        'book': book,
        'reviews': reviews,
        'review_form': review_form,
        'reply_form': ReplyForm(),
    }
    return render(request, 'book/book_detail.html', context)


@login_required
@require_POST
def add_reply(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    reply_form = ReplyForm(request.POST)
    if reply_form.is_valid():
        reply = reply_form.save(commit=False)
        reply.review = review
        reply.user = request.user
        reply.save()
        messages.success(request, "پاسخ شما ثبت شد 💬")
    return redirect('book_detail', id=review.book.id)