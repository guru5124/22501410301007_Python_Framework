from django import forms
from .models import ContactUs, Post, Category, Registration

# CONTACT US FORM

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

# LOGIN FORM

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

# POST FORM

class PostForm(forms.ModelForm):

    is_published = forms.ChoiceField(
        choices=[
            (True, "Yes"),
            (False, "No")
        ],
        widget=forms.RadioSelect
    )

    class Meta:
        model = Post
        fields = '__all__'

# CATEGORY FORM

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

# REGISTRATION FORM 
class RegistrationForm(forms.ModelForm):

    re_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registration
        fields = ['name', 'user_name', 'mobile_no', 'password']

        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password and re_password and password != re_password:
            raise forms.ValidationError("Password and Confirm Password do not match!")

        return cleaned_data