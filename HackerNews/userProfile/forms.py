from django import forms


class UserForm(forms.Form):
    about = forms.CharField(label="about", widget=forms.Textarea, required=False)
    email = forms.EmailField(label="email", required=False)
