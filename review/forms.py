from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    rating = forms.ChoiceField(choices=[(5, '5 звезд'), (4, '4 звезды'), (3, '3 звезды'), (2, '2 звезды'), (1, '1 звезда')], widget=forms.Select(attrs={'required': 'required'}))
    review = forms.CharField(widget=forms.Textarea(attrs={'required': 'required'}))
    url_game = forms.IntegerField(widget=forms.HiddenInput())