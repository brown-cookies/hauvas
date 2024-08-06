from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control form-control-xl",
                "placeholder": "Username",
                "required": True,
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "form-control form-control-xl",
                "placeholder": "Password",
                "required": True,
            }
        )
    )

    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input me-2"},
        ),
        initial=True,
        required=False,
    )
