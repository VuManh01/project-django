# patients/views.py

from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm

# View để thêm bệnh nhân
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()  # Tự động lưu dữ liệu vào database
            return redirect('patients_list')
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form': form})

# View hiển thị danh sách bệnh nhân
def patients_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients_list.html', {'patients': patients})
