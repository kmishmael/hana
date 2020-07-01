from django import forms

from social.models import Platforms

class PlatfromForm(forms.ModelForm):
    class meta:
        model = Platforms
        field = ['s_name','p_email','p_username','p_password','f_class']
        