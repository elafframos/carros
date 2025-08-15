from django import forms
from .models import Car

class Formulario(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'meu-input'}),
            'marca': forms.TextInput(attrs={'class': 'meu-input'}),
            'ano': forms.NumberInput(attrs={'class': 'meu-input'}),
            'value': forms.NumberInput(attrs={'class': 'meu-input'}),
            'imagem': forms.FileInput(attrs={'class': 'meu-input-arquivo'}),
        }

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro é de R$ 20.000 reais.')
        return value
