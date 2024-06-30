from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Owner, Patient
from .forms import OwnerCreateForm, PatientCreateForm

def home(request):
   context = {"name": "Djangoer"}
   return render(request, 'vetoffice/home.html', context)

class OwnerList(ListView):
   model = Owner

class OwnerCreate(CreateView):
   model = Owner
   template_name = 'vetoffice/owner_create_form.html'
   form_class = OwnerCreateForm

class PatientList(ListView):
   model = Patient

class PatientCreate(CreateView):
   model = Patient
   template_name = "vetoffice/patient_create_form.html"
   form_class = PatientCreateForm
