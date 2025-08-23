from django import forms
from .models import Car
class Formulario(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'model': forms.TextInput(attrs={'class': 'input-modelo'}),
            'brand': forms.Select(attrs={'class': 'input-marca'}),
            'factory_year': forms.NumberInput(attrs={'class': 'input-ano-fabricacao'}),
            'model_year': forms.NumberInput(attrs={'class': 'input-ano-modelo'}),
            'value': forms.NumberInput(attrs={'class': 'input-preco'}),
            'photo': forms.FileInput(attrs={'class': 'input-foto'}),
        }


    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro é de R$ 20.000 reais.')
        return value
