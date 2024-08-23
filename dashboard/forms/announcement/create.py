from django import forms
from announcement.models import Announcement


class CreateAnnouncementForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Announcement Title..."}
        )
    )

    content = forms.CharField(widget=forms.Textarea(attrs={"class": "d-none"}))

    class Meta:
        model = Announcement
        fields = ["title", "content"]
