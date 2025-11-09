from operator import attrgetter
from django import forms

from accounts.models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=20,
        label="نام کاربری",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        max_length=20,
        label="گذرواژه",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
            "bio",
            "birthdate",
            "profile_pic",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
            'email' : forms.TextInput(attrs={"class": "form-control"}),
            "birthdate": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "bio": forms.Textarea(attrs={"class": "form-control", "row": 5}),
            "profile_pic": forms.FileInput(attrs={"class": "form-control"}),
        }
