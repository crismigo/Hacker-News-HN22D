from django import forms

from news.models import Submission


class SubmissionForm(forms.Form):
    title = forms.CharField(label="title", required=True)
    url = forms.CharField(label="url", required=False, max_length=100)
    text = forms.CharField(label="text", widget=forms.Textarea, required=False)

    class Meta:
        model = Submission

    def clean(self):
        cd = self.cleaned_data
        if cd.get('url') == "" and cd.get('text') == "":
            self.add_error('url', "Url or text requiered")
        if cd.get('url') != "" and not isValidUrl(cd.get('url')):
            self.add_error('url', "The Url is not valid")
        return cd


def isValidUrl(url):
    import re
    regex = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url is not None and regex.search(url)
