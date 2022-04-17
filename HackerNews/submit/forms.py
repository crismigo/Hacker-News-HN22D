from django import forms

from news.models import Submission


class SubmissionForm(forms.Form):
    title = forms.CharField(label="title", required=True)
    url = forms.CharField(label="url", required=False)
    text = forms.CharField(label="text", widget=forms.Textarea, required=False)

    class Meta:
        model = Submission

    def clean(self):
        cd = self.cleaned_data
        if cd.get('url') == "" and cd.get('text') == "":
            print("holi")
            self.add_error('url', "Url or text requiered")
        return cd
