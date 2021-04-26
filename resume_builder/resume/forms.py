from django import forms
from .models import Person, Education, Experience, Other, personal_info, contact,Letter



class PersonForm(forms.ModelForm):

    class Meta:

        model = Person
        fields = ['picture','name','occupation','about_Me']

class LetterForm(forms.ModelForm):

    class Meta:

        model = Letter
        fields = ['author','recepient','date','formulation','text','stamp']
        widgets = {'date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}



class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ['institution','level','detail','start_date','end_date','description']
        widgets = {'start_date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'end_date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}


class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience        
        fields = ['job_title','company','job_detail','start_Date','end_Date','job_description']
        widgets = {'start_Date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'end_Date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}


    

class OtherForm(forms.ModelForm):

    class Meta:
        model = Other
        fields = ['extra_title','extra_subtitle','extra_detail','startDate','endDate','extra_description']
        widgets = {'startDate':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'endDate':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}


class ContactForm(forms.ModelForm):

    class Meta:
        model = contact
        fields = ['website','email','phone','address']

class InfoForm(forms.ModelForm):

    class Meta:
        model = personal_info
       
      

        fields = ['nationality','residency','languages','birthday']
        widgets = {'birthday':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}

