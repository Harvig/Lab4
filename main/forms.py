from django import forms
from main.models import Putovanje

class PutovanjeForm(forms.ModelForm):
    class Meta:
        model = Putovanje
        fields = '__all__'  
    
    def clean_putovanje_cijena(self):
        cijena = self.cleaned_data.get('putovanje_cijena')
        if cijena <= 0:
            raise forms.ValidationError("Cijena must be greater than zero.")
        return cijena
