from django.forms import ModelForm
from .models import Curdmodel1,EmailSendModel,FormSetModel
from django import forms
from django.core.exceptions import ValidationError
#from django.core import validators
from django.core import validators
from django.core.mail import EmailMessage

class CurdForm(forms.ModelForm):
    
    class Meta:
        model=Curdmodel1
        fields='__all__'#['Select','Ename','Subject','Sal','Date_of_birth','Gender','Distric','Technologies','Search','File','User_Image','Passed']
        #'Email']#'From','To','Subject','Attach','Message']
        widgets = {
            'Date_of_birth':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            
            'Message':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write the messae'})
           }
    # def _clean_subject(self):
    #     Subject = self.cleaned_data.get('Subject')
    #     return Subject

    # def clean_Email(self):
    #     Email = self.cleaned_data.get('Email', False)
    #     if [len(Email)-9]!='gmail.com':
    #         raise ValidationError(('email does not match'),params={'Email':Email}) 

    # def clean_email(self):
    #     email = self.cleaned_data.get('Email')
    #     return email


    # def clean_message(self):
    #     Message = self.cleaned_data.get('Message')
    #     return Message

    # def clean_attach(self):
    #     Attach = self.cleaned_data.get('Attach')
    #     return Attach

    # def clean_Ename(self):
    #     name = self.cleaned_data.get("Ename")
    #     print(name)
    #     if name.upper() == "HELLO":
    #         raise forms.ValidationError("Not a valid name")
    #     return name
    # def clean(self):
    #     total_clean_data=super().clean()
    #     name=total_clean_data['Ename']
    #     if name[0].lower()!='c':
    #         raise forms.ValidationError("Name should be start with c letter")

    # def clean_image(self):
    #         Ename = self.cleaned_data.get('Ename', False)
    #         if Ename[0].lower()!='c':
    #             raise ValidationError("name not valid")
    #         return None


class EmailSendForm(forms.ModelForm):
    # class Meta:
    #     model=EmailSendModel
    #     fields='__all__'

    


    
class FormSetForm(forms.Form):
    Name=forms.CharField(max_length=20)
    Date=forms.DateField()

