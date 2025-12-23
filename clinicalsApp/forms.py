from django import forms
from clinicalsApp.models import clinicalData, Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class clinicalDataForm(forms.ModelForm):
    class Meta:
        model = clinicalData
        fields = '__all__'