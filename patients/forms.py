# patients/forms.py

from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):  # Đảm bảo thừa kế từ ModelForm
    class Meta:
        model = Patient  # Liên kết với model Patient
        fields = ['name', 'phone', 'disease']  # Các trường cần sử dụng trong form
