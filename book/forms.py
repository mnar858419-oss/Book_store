from pydoc import describe
from django import forms
from book.models import Author, Book , Review , Reply


class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label="عنوان",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mt-2",
            }
        ),
    )
    description = forms.CharField(
        max_length=255,
        label="توضیحات",
        widget=forms.Textarea(attrs={"class": "form-control mt-2"}),
    )

    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #     if len(name) < 5:
    #         raise forms.ValidationError(
    #             "این فیلد نمی تواند کمتر از ۵ کاراکتر داشته باشد"
    #         )
    #     return name

    # def clean_description(self):
    #     d = self.cleaned_data.get("description")
    #     if len(d) > 10:
    #         raise forms.ValidationError("خیلی طولانیه")

    #     return d

    def clean(self):
        name = self.cleaned_data.get("name")
        description = self.cleaned_data.get("description")

        if name == description:
            raise forms.ValidationError("نام با توضیحات نمی تواند یکسان باشد")
        return self.cleaned_data


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "birthdate", "biography"]

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "last_name": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "birthdate": forms.DateInput(attrs={"class": "form-control mt-2"}),
            "biography": forms.Textarea(attrs={"class": "form-control mt-2"}),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "category",
            "published_day",
            "pages",
            "summary",
            "cover",
        ]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control mt-2"}),
            "author": forms.Select(attrs={"class": "form-control mt-2"}),
            "category": forms.Select(attrs={"class": "form-control mt-2"}),
            "published_day": forms.DateInput(
                attrs={"class": "form-control mt-2", "type": "date"}
            ),
            "pages": forms.NumberInput(attrs={"class": "form-control mt-2"}),
            "cover": forms.FileInput(attrs={"class": "form-control mt-2"}),
            "summary": forms.Textarea(attrs={"class": "form-control mt-2"}),
        }

    # def clean_title(self):
    #     title = self.cleaned_data.get("title")
    #     if len(title) < 10:
    #         raise forms.ValidationError("این فیلد نمی تواند کمتر از ۱۰ کاراکتر باشد")
    #     return title

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',       # ظاهر بوت‌استرپ
        }),
        label='امتیاز شما'
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'نظر خود را بنویسید...',
                'class': 'form-control'
            }),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'پاسخ خود را بنویسید...',
                'class': 'form-control'
            }),
        }