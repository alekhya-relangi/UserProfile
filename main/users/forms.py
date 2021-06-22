from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.contrib.auth import forms
from phonenumber_field.formfields import PhoneNumberField

class CustomUserCreationForm(UserCreationForm):
    phone=PhoneNumberField(required=True)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email","phone",)
        
class UserDeleteForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields ='__all__'
        