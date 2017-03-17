from django import forms


class ArtistForm(forms.Form):
    name = forms.CharField(label='Artist Name ', max_length=300,
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': "Enter Artist's name",
                                   'class': "form-control",
                                   'style': "width: 300px;"
                               })
                           )
