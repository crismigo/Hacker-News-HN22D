from django import forms


class SubmissionForm(forms.Form):
    title = forms.CharField(label="title", required=True)
    url = forms.CharField(label="url", required=False)
    text = forms.CharField(label="text", widget=forms.Textarea, required=False)
