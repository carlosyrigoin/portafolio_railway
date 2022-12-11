from django import forms

class PortafolioForm(forms.Form):
    titulo = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    descripcion = forms.CharField(max_length=254, widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    tags = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    foto = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "class": "form-control mb-3", "type":"url"
    }))
    urlgithub = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "class": "form-control mb-3", "type":"url"
    }))