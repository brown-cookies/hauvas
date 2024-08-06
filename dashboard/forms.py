from django import forms
from .models import Course, ModuleList, ModuleItem


class UpdateCourseAboutForm(forms.ModelForm):

    about = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "type": "text",
                "class": "form-control d-none",
                "placeholder": "Update your 'About the Course' here...",
                # TODO: Remove value after testing
                "value": "Test value for About",
                "required": True,
            }
        ),
    )

    class Meta:
        model = Course
        fields = ["about"]


class UpdateCourseSyllabusForm(forms.ModelForm):

    syllabus = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "type": "text",
                "class": "form-control d-none",
                "placeholder": "Update your 'syllabus' here...",
                # TODO: Remove value after testing
                "value": "Test value for syllabus",
                "required": True,
            }
        ),
    )

    class Meta:
        model = Course
        fields = ["syllabus"]


class UpdateModuleListForm(forms.ModelForm):
    class Meta:
        model = ModuleList
        fields = ["title"]


class UpdateModuleItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        module_item = kwargs.pop("module_item", "")

        super(UpdateModuleItemForm, self).__init__(*args, **kwargs)

        self.fields["title"] = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control", "placeholder": module_item.title}
            )
        )
        self.fields["short_description"] = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": module_item.short_description,
                }
            )
        )
        self.fields["description"] = forms.CharField(
            widget=forms.Textarea(
                attrs={"class": "form-control", "placeholder": module_item.description}
            )
        )
        self.fields["content_url"] = forms.CharField(
            widget=forms.TextInput(
                attrs={"class": "form-control", "placeholder": module_item.content_url}
            )
        )
        self.fields["is_published"] = forms.CharField(
            widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
            required=False,
            initial=module_item.is_published,
        )

    class Meta:
        model = ModuleItem
        fields = [
            "title",
            "short_description",
            "description",
            "content_url",
            "is_published",
        ]
