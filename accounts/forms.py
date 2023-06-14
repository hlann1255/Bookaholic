from django import forms 
from .models import Account 

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Nhập mật khẩu của bạn',
        'class': 'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Nhập lại mật khẩu của bạn',
    }))
    class Meta:
        model = Account 
        fields = ['first_name','last_name','phone_number','email','password'] 

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nhập họ của bạn'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nhập tên của bạn'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Nhập số điện thoại của bạn'
        self.fields['email'].widget.attrs['placeholder'] = 'Nhập email của bạn' 
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean() 
        password = cleaned_data.get('password') 
        confirm_password  = cleaned_data.get('confirm_password') 

        if password != confirm_password:
            raise forms.ValidationError("Mật khẩu không trùng khớp") 

        