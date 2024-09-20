from .models import Event
from django import forms


class AddEventForm(forms.ModelForm):

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Event Title"}
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Event Description"}
        )
    )

    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Event Start Date",
                "type": "date",
            }
        )
    )

    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "placeholder": "Event End Date",
                "type": "date",
            }
        )
    )

    start_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Event Start Time",
                "type": "time",
            }
        )
    )

    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "class": "form-control",
                "placeholder": "Event End Time",
                "type": "time",
            }
        )
    )

    class Meta:
        model = Event
        fields = [
            "title",
            "description",
            "start_date",
            "end_date",
            "start_time",
            "end_time",
        ]
