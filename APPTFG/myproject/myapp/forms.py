from django import forms
from .models import Objetivo, Indicador, AGC, UGC, AcuerdoIndicadores


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'id_ugc', 'perfil', 'descripcion_usuario')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class ObjetivoForm(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = '__all__'

class IndicadorForm(forms.ModelForm):
    class Meta:
        model = Indicador
        fields = '__all__'

class AGCForm(forms.ModelForm):
    class Meta:
        model = AGC
        fields = '__all__'

class UGCForm(forms.ModelForm):
    class Meta:
        model = UGC
        fields = '__all__'

class AcuerdoIndicadoresForm(forms.ModelForm):
    class Meta:
        model = AcuerdoIndicadores
        fields = '__all__'


class UploadExcelForm(forms.Form):
    excel_file = forms.FileField(label='Seleccione un archivo Excel')

class AGCForm(forms.ModelForm):
    class Meta:
        model = AGC
        fields = ['id_ugc', 'anio_agc', 'descripcion_agc']
        widgets = {
            'anio_agc': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
            'id_ugc': forms.Select(attrs={'class': 'form-control'}),
            'descripcion_agc': forms.TextInput(attrs={'class': 'form-control'}),
        }