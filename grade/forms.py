from .models import Activity, Exam, StudentActivity, StudentExam
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


class StudentActivityForm(forms.ModelForm):

    score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))

    class Meta:
        model = StudentActivity
        fields = ["score"]


class StudentExamForm(forms.ModelForm):

    score = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))

    class Meta:
        model = StudentExam
        fields = ["score"]
