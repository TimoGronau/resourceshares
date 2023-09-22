from django import forms
from .utils import generate_category_iterable, generate_tag_iterable


class PostResourceForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "title-input",
                "placeholder": "Enter a title",
            }
        )
    )  # type='text'
    link = forms.URLField()  # type='url'
    description = forms.CharField(widget=forms.Textarea)  # type='textarea'
    category = forms.ChoiceField(widget=forms.RadioSelect, choices=generate_category_iterable)
    tags = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=generate_tag_iterable, required=False)
    
#good way to create form
# CATEGORIES = [
#     ("1", "Programming Language"),
#     ("2", "Databases")
# ]