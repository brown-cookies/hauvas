from django import forms


class UpdateAnnouncementForm(forms.Form):

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
