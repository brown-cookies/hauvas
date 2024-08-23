from django import forms


class SyllabusUpdateForm(forms.Form):
    syllabus = forms.CharField(widget=forms.Textarea(attrs={"class": "d-none"}))
