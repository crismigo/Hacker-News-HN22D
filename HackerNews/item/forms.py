from django import forms


class ShowSubmissionComment(forms.Form):
    comment = forms.CharField(label="", widget=forms.Textarea, required=True)
