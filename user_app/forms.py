from django import forms
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmation du mot de passe', widget=forms.PasswordInput)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'date_of_birth', 'can_be_contacted', 'can_data_be_shared']
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Les mots de passe ne correspondent pas.")
        
        return cleaned_data
