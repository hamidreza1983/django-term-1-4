from django import forms
from .models import ContactUs


#class ContactUsForm(forms.Form):
#    name = forms.CharField(max_length=100)
#    email = forms.EmailField()
#    subject = forms.CharField(max_length=100)
#    message = forms.CharField(widget=forms.Textarea(attrs={"rows":6}))

class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']