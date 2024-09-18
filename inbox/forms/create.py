from django import forms
from django.contrib.auth import get_user_model
from inbox.models import Inbox

User = get_user_model()


class ComposeInboxForm(forms.Form):

    receiver = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "To"})
    )

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Subject"}
        )
    )

    content = forms.CharField(widget=forms.Textarea(attrs={"class": "d-none"}))
