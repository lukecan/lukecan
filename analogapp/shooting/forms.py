from django import forms
from .models import Film, CekimKosulu, Poz

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['name', 'iso']

class CekimKosuluForm(forms.ModelForm):
    class Meta:
        model = CekimKosulu
        fields = ['aydinlatma', 'hava_durumu']

class PozForm(forms.ModelForm):
    class Meta:
        model = Poz
        fields = ['film', 'kosul', 'tarih', 'notlar']
