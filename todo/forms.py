from .models import Todo
from django import forms


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter todo title here"}
            ),
        }
