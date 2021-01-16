from django import forms
from django.core import validators
class signup(forms.Form):
    name=forms.CharField()
    roll=forms.IntegerField()
    email=forms.EmailField()
    phone=forms.CharField()
    comments=forms.CharField(widget=forms.Textarea)
    password=forms.CharField(widget=forms.PasswordInput)
    areuengineeringstudent=forms.BooleanField()
    repassword=forms.CharField(label="re-enter the password", widget=forms.PasswordInput)
    def clean(self):
        entire_data=super().clean()
        n=entire_data['name']
        if (len(n)>10):
            raise forms.ValidationError("enter character less than 10")
        r=entire_data['roll']
        if (r<0):
            raise forms.ValidationError("negative rollno in valid")
        p=entire_data['password']  
        rp=entire_data['repassword']
        if (p!=rp):
            raise forms.ValidationError("mismatch in passowrd")  
