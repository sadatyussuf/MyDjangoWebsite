from django import forms
from django.forms import models
from django.forms import fields
from .models import Article

class Create_Article(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','body','thumb']


# #Will work on it later

# class ContactForm(forms.Form):
#     from_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)


class ContactForm(forms.Form):
    BUG = 'b'
    FEEDBACK = 'fb'
    NEW_FEATURE = 'nf'
    OTHER = 'o'
    purpose_choices = (
        (FEEDBACK, 'Feedback'),
        (NEW_FEATURE, 'Feature Request'),
        (BUG, 'Bug'),
        (OTHER, 'Other'),
    )

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    purpose = forms.ChoiceField(choices=purpose_choices)
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}),required=True)
