from django import forms
from django.contrib.auth.password_validation import validate_password
from myapp.models import myUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
        help_text="Your password must contain at least 8 characters.",
    )

    class Meta:
        model = myUser
        fields = ['username', 'password', 'is_admin', 'is_regional_head', 'is_activity_head', 'is_sub_regional_head', 'region', 'activity', 'sub_region']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password
