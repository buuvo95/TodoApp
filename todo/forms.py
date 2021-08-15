from django import forms
from django.db.models import fields
from .models import Category, Todo

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            "category",
            "description",
            "date_begin",
            "check"
        )

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = (
            "name",
            "description",
            "date_begin",
            "date_end",
            "check",
            "category",
        )