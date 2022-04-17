from django import forms

from news.models import Submission


class SubmissionForm(forms.Form):
    title = forms.CharField(label="title", required=True)
    url = forms.CharField(label="url", required=False)
    text = forms.CharField(label="text", widget=forms.Textarea, required=False)

    class Meta:
        model = Submission
