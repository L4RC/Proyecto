from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions
from django import forms
from .models import CustomUser
from django.forms.widgets import SelectDateWidget, DateInput


class RegistrationForm(forms.ModelForm):
    Contraseña = forms.CharField(widget=forms.PasswordInput)
    Confirmacion = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    #Fecha = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget(years=range(1940, 2005)))
    Fecha = forms.DateField(
        label='Fecha de Nacimiento', widget=DateInput(attrs={'type': 'date'}),)

    class Meta:
        model = CustomUser
#        fields = ('username', 'password', 'nombre', 'correo', 'telefono', 'edad')
        fields = ('Nombre', 'Apellido','DPI','Fecha','Telefono','Usuario','Correo','Contraseña','Confirmacion')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
            'Nombre',
            'Apellido',
            'DPI',
            'Fecha de nacimiento',
            'Telefono',
            'Nombre de usuario',
            'Correo electróinco',
            'Contraseña',
            'Confirmacion',
            FormActions(
                Submit('submit', 'Registrarse', css_class='btn btn-primary')
            )
        )
