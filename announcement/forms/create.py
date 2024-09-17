from dashboard.models import Course
from django import forms


class CreateAnnouncementForm(forms.Form):

    course = forms.ModelChoiceField(
        widget=forms.Select(attrs={"class": "form-select"}),
        queryset=Course.objects.none(),
        empty_label="Select Course",
    )

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

    def __init__(self, *args, **kwargs):

        user = kwargs.pop("user", None)
        super(CreateAnnouncementForm, self).__init__(*args, **kwargs)

        if user is not None:
            self.fields["course"].queryset = Course.objects.filter(
                professor=user.professor
            )

    class Meta:
        fields = []
