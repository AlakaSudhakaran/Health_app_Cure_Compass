from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Symptom, UserSymptomReport, CustomUser

# Define CustomUserCreationForm with additional fields: age, gender, and terms
class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField(required=True, label="Age")
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], label="Gender")
    terms = forms.BooleanField(required=True, label="Agree to terms and conditions")  # Checkbox for terms

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'age', 'gender', 'terms')

    # Validation to ensure the 'terms' checkbox is checked
    def clean_terms(self):
        terms = self.cleaned_data.get('terms')
        if not terms:
            raise forms.ValidationError("You must agree to the terms and conditions.")
        return terms

# Symptom report form that allows users to select multiple symptoms
class SymptomReportForm(forms.Form):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Symptoms"
    )

    def save(self, user):
        report = UserSymptomReport.objects.create(user=user)
        report.symptoms.set(self.cleaned_data['symptoms'])
        return report

# Symptom selection form to choose multiple symptoms for reporting
class SymptomSelectionForm(forms.Form):
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Select Symptoms"
    )

from django import forms

class MedicalHistoryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    age = forms.IntegerField(label='Age')
    medical_history = forms.CharField(label='Medical History', widget=forms.Textarea)
    height = forms.DecimalField(label='Height (in cm)', decimal_places=2, max_digits=5)
    weight = forms.DecimalField(label='Weight (in kg)', decimal_places=2, max_digits=5)
    blood_group = forms.ChoiceField(
        label='Blood Group',
        choices=[
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-')
        ]
    )

