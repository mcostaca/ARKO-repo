from django import forms
from django_select2.forms import ModelSelect2Widget
from .models.localidades import Municipio, Distrito, Estado

class EstadoSelectForm(forms.Form):
    estado = forms.ModelChoiceField(
        queryset=Estado.objects.all(),
        required=False,
        label='Estado',
        widget=ModelSelect2Widget(
            model=Estado,
            search_fields=['nome__icontains'],
            attrs={'data-placeholder': 'Digite o estado',
            'style': 'width: 100%;'}
        )
    )

class DistritoSelectForm(forms.Form):
    distrito = forms.ModelChoiceField(
        queryset=Distrito.objects.all(),
        required=False,
        label='Distrito',
        widget=ModelSelect2Widget(
            model=Distrito,
            search_fields=['nome__icontains'],
            attrs={'data-placeholder': 'Digite o distrito',
            'style': 'width: 100%;'}
        )
    )


class MunicipioSelectForm(forms.Form):
    municipio = forms.ModelChoiceField(
        queryset=Municipio.objects.all(),
        required=False,
        label='Município',
        widget=ModelSelect2Widget(
            model=Municipio,
            search_fields=['nome__icontains'],
            attrs={'data-placeholder': 'Digite o município',
            'style': 'width: 100%;'}
        )
    )
