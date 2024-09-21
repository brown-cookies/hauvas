from .models import Activity, Exam
from django import forms


class AddActivityForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Activity Name..."}
        )
    )

    score = forms.CharField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Activity Score..."}
        )
    )

    class Meta:
        model = Activity
        fields = ["name", "score"]


class AddExamForm(forms.ModelForm):

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Activity Name..."}
        )
    )

    score = forms.CharField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Activity Score..."}
        )
    )

    class Meta:
        model = Exam
        fields = ["name", "score"]
