from django import forms
from announcement.models import Announcement


class CreateAnnouncementForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Announcement Title..."}
        )
    )

    short_description = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Short description..."}
        )
    )

    content = forms.CharField(widget=forms.Textarea(attrs={"class": "d-none"}))

    class Meta:
        model = Announcement
        fields = ["title", "short_description", "content"]
