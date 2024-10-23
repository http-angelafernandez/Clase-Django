from django import forms

class CrearLibroFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    genero = forms.CharField(max_length=30)
    autor = forms.CharField(max_length=30)

class BuscarLibroFormulario(forms.Form):
    nombre = forms.CharField(required=False)  
    genero = forms.CharField(required=False)  