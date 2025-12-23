from django.shortcuts import render, redirect
from clinicalsApp.models import Patient, clinicalData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clinicalsApp.forms import clinicalDataForm

# Create your views here.
class PatientListView(ListView):
    model = Patient
    
class PatientCreateView(CreateView):
    model = Patient
    fields = ['last_name', 'first_name', 'age']
    success_url = reverse_lazy('index')
    
class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['last_name', 'first_name', 'age'] 
    success_url = reverse_lazy('index')
    
class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')
    
def addData(request, **kwargs):
    form = clinicalDataForm()
    patient = Patient.objects.get(id=kwargs.get('pk'))
    if request.method == 'POST':
        form = clinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalsApp/clinicaldata_form.html', {'form': form, 'patient': patient})

def analyze(request, **kwargs):
    pk = kwargs.get('pk')
    data = clinicalData.objects.filter(patient_id=pk)
    responseData = []
    for eachEntry in data:
        responseData.append(eachEntry)
        if eachEntry.compponentName == 'hw':
            heightAndWeight = eachEntry.measuredValue.split('/')
            if len(heightAndWeight) > 1:
                heightInMeters = float(heightAndWeight[0]) * 0.0254
                weightInKg = float(heightAndWeight[1]) * 0.453592
                bmi = weightInKg / (heightInMeters * heightInMeters)
                bmiEntry = clinicalData(
                    compponentName='BMI',
                    measuredValue=str(bmi),
                    patient_id=pk
                )
                responseData.append(bmiEntry)
    return render(request, 'clinicalsApp/generateReport.html', {'data': responseData})