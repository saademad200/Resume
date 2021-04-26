from django import forms
from .models import Person, Education,Education2,Education3, Experience,Experience2,Experience3, Other, personal_info, contact,Letter



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

class Education2Form(forms.ModelForm):

    class Meta:
        model = Education2
        fields = ['institution2','level2','detail2','start_date2','end_date2','description2']
        widgets = {'start_date2':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'end_date2':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}
class Education3Form(forms.ModelForm):

    class Meta:
        model = Education3
        fields = ['institution3','level3','detail3','start_date3','end_date3','description3']
        widgets = {'start_date3':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'end_date3':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}

class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience        
        fields = ['job_title','company','job_detail','start_Date','end_Date','job_description']
        widgets = {'start_Date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'end_Date':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}


class Experience2Form(forms.ModelForm):

    class Meta:
        model = Experience2      
        fields = ['job_title2','company2','job_detail2','start_Date2','end_Date2','job_description2']
        widgets = {'start_Date2':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'end_Date2':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}


class Experience3Form(forms.ModelForm):

    class Meta:
        model = Experience3        
        fields = ['job_title3','company3','job_detail3','start_Date3','end_Date3','job_description3']
        widgets = {'start_Date3':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),'end_Date3':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),}


    

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

