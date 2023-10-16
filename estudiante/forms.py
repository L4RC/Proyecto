from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FormActions
from django import forms
from .models import CustomUser
from django.forms.widgets import SelectDateWidget, DateInput


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    #Fecha = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget(years=range(1940, 2005)))
    Fecha = forms.DateField(
        label='Fecha de Nacimiento', widget=DateInput(attrs={'type': 'date'}),)

    class Meta:
        model = CustomUser
#        fields = ('username', 'password', 'nombre', 'correo', 'telefono', 'edad')
        fields = ('first_name', 'last_name','DPI','Fecha','Telefono','username','email','password','password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'
        self.helper.layout = Layout(
            'first:name',
            'last_name',
            'DPI',
            'Fecha de nacimiento',
            'Telefono',
            'username',
            'email',
            'password',
            'password2',
            FormActions(
                Submit('submit', 'Registrarse', css_class='btn btn-primary')
            )
        )
