from django import forms

from news.models import Submission


class ShowSubmissionComment(forms.Form):
    comment = forms.CharField(label="", widget=forms.Textarea, required=True)


class EditForm(forms.ModelForm):

    class Meta:
        model = Submission
        fields = ("title","url","text")
        widgets = {
            'url' : forms.TextInput(attrs={'disabled': True})
        }



