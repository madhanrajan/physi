from django import forms
from .models import FeedbackData


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackData
        fields = ["data"]
