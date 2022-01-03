from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = [
            "title",
            "description"
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ("text",)

        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control"})
        }