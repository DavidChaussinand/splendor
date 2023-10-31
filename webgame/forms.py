from django import forms


class TokenForm(forms.Form):
    red = forms.BooleanField(label="red", required= False)
    blue = forms.BooleanField(label="blue", required= False)
    black = forms.BooleanField(label="black", required= False)
    white = forms.BooleanField(label="white", required= False)
    green = forms.BooleanField(label="green", required= False)

    def clean(self):
        cleaned_data=super().clean()