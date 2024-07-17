from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "username"}
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password"}
        ),
    )
    password2 = forms.CharField(
        label="Повтор пароля",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password confirmation"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "username"}
        ),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password"}
        ),
    )

    class Meta:
        fields = ("username", "password")
