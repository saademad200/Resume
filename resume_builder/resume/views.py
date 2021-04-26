from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.requests import RequestSite
from .utils import getPDF
import cv2
from django.conf import settings
import numpy as np
from PIL import Image

from .forms import PersonForm, EducationForm,Education2Form,Education3Form, ExperienceForm,Experience2Form,Experience3Form, OtherForm, ContactForm, InfoForm,LetterForm


def resumeFill(request):
    if request.method == 'POST':
        personform = PersonForm(request.POST,request.FILES)
        educationform = EducationForm(request.POST)
        education2form = Education2Form(request.POST)
        education3form = Education3Form(request.POST)
        experienceform = ExperienceForm(request.POST)
        experience2form = Experience2Form(request.POST)
        experience3form = Experience3Form(request.POST)
        otherform = OtherForm(request.POST)
        infoform = InfoForm(request.POST)
        contactform = ContactForm(request.POST)
        letterform = LetterForm(request.POST,request.FILES)
        
       
        if personform.is_valid() and bool(request.FILES):
            
            
            filename = personform.cleaned_data['picture']
            pil_img = Image.open(filename)
            cv_img = np.array(pil_img)
            if cv_img.shape[2]==4 and np.mean(cv_img[:,:,0:2]) == 0:
              
              cv_img = cv2.bitwise_not(cv_img)
              cv2.imwrite(settings.MEDIA_ROOT+'/photo.jpg',cv_img[:,:,3])
              personform.cleaned_data['picture']='photo.jpg'
              
            
            else:
              cv2.imwrite(settings.MEDIA_ROOT+'/photo.jpg',cv_img[:,:,::-1])
              personform.cleaned_data['picture']='photo.jpg'
              
        if letterform.is_valid() and bool(request.FILES):
            filename = letterform.cleaned_data['stamp']
            pil_img = Image.open(filename)
            cv_img = np.array(pil_img)
            if cv_img.shape[2]==4 and np.mean(cv_img[:,:,0:2]) == 0:
              
              cv_img = cv2.bitwise_not(cv_img)
              cv2.imwrite(settings.MEDIA_ROOT+'/stamp.jpg',cv_img[:,:,3])
              letterform.cleaned_data['stamp']='stamp.jpg'
            else:
              cv2.imwrite(settings.MEDIA_ROOT+'/stamp.jpg',cv_img[:,:,::-1])
              letterform.cleaned_data['stamp']='stamp.jpg'

        if (
            educationform.is_valid() and education2form.is_valid() and 
            education3form.is_valid() and  personform.is_valid() 
            and experienceform.is_valid() and experience2form.is_valid()
            and experience3form.is_valid() and otherform.is_valid() 
            and infoform.is_valid() and contactform.is_valid() 
            and letterform.is_valid()
             ):
            data = {
                'photo':settings.MEDIA_ROOT+"/"+ personform.cleaned_data['picture'],
                'title':personform.cleaned_data['name'],
                'subtitle':personform.cleaned_data['occupation'],
                'description':personform.cleaned_data['about_Me']
                }
            contact = [
                {'address':contactform.cleaned_data['address']},
                {'email':contactform.cleaned_data['email']},
                {'phone':contactform.cleaned_data['phone']},
                {'website':contactform.cleaned_data['website']}
            ]
            data['contact'] = contact

            personal_info = [
                {'birthday':infoform.cleaned_data['birthday']},
                {'nationality':infoform.cleaned_data['nationality']},
                {'residency':infoform.cleaned_data['residency']},
                {'languages':infoform.cleaned_data['languages'].split(',')}
            ]
            data['personal_info'] = personal_info

            letter ={
                "date":f"{letterform.cleaned_data['date'].day}-{letterform.cleaned_data['date'].month}-{letterform.cleaned_data['date'].year}",
                "recipient":letterform.cleaned_data['recepient'],
                "text":letterform.cleaned_data['text'],
                "author":letterform.cleaned_data['author'],
                "stamp":settings.MEDIA_ROOT+"/"+letterform.cleaned_data['stamp'],
                "formulation":letterform.cleaned_data['formulation']
            } 
            data['letter'] = letter

            curriculum = []
            experience = [
                {
                  'title':experienceform.cleaned_data['company'],
                  'subtitle':experienceform.cleaned_data['job_title'],
                  'detail':experienceform.cleaned_data['job_detail'],
                  'description':experienceform.cleaned_data['job_description'], 
                  'highlight':True,
                  'date': f"{experienceform.cleaned_data['start_Date'].year}-{experienceform.cleaned_data['end_Date'].year}"
                },
                {
                  'title':experience2form.cleaned_data['company2'],
                  'subtitle':experience2form.cleaned_data['job_title2'],
                  'detail':experience2form.cleaned_data['job_detail2'],
                  'description':experience2form.cleaned_data['job_description2'], 
                  'highlight':True,
                  'date': f"{experience2form.cleaned_data['start_Date2'].year}-{experience2form.cleaned_data['end_Date2'].year}"
                },
                {
                  'title':experience3form.cleaned_data['company3'],
                  'subtitle':experience3form.cleaned_data['job_title3'],
                  'detail':experience3form.cleaned_data['job_detail3'],
                  'description':experience3form.cleaned_data['job_description3'], 
                  'highlight':True,
                  'date': f"{experience3form.cleaned_data['start_Date3'].year}-{experience3form.cleaned_data['end_Date3'].year}"
                }
            ]
            Experience_={}
            Experience_['Experience']=experience
            education = [
                {
                  'title':educationform.cleaned_data['institution'],
                  'subtitle':educationform.cleaned_data['level'],
                  'detail':educationform.cleaned_data['detail'],
                  'description':educationform.cleaned_data['description'], 
                  'highlight':True,
                  'date': f"{educationform.cleaned_data['start_date'].year}-{educationform.cleaned_data['end_date'].year}"
                },
                {
                  'title':education2form.cleaned_data['institution2'],
                  'subtitle':education2form.cleaned_data['level2'],
                  'detail':education2form.cleaned_data['detail2'],
                  'description':education2form.cleaned_data['description2'], 
                  'highlight':True,
                  'date': f"{education2form.cleaned_data['start_date2'].year}-{education2form.cleaned_data['end_date2'].year}"
                },
                {
                  'title':education3form.cleaned_data['institution3'],
                  'subtitle':education3form.cleaned_data['level3'],
                  'detail':education3form.cleaned_data['detail3'],
                  'description':education3form.cleaned_data['description3'], 
                  'highlight':True,
                  'date': f"{education3form.cleaned_data['start_date3'].year}-{education3form.cleaned_data['end_date3'].year}"
                }
            ]
            Education_={}
            Education_['Education']=education

            other = [
                {
                  'title':otherform.cleaned_data['extra_title'],
                  'subtitle':otherform.cleaned_data['extra_subtitle'],
                  'detail':otherform.cleaned_data['extra_detail'],
                  'description':otherform.cleaned_data['extra_description'], 
                  'highlight':True,
                  'date': f"{otherform.cleaned_data['startDate'].year}-{otherform.cleaned_data['endDate'].year}"
                }
            ]
            Other_={}
            Other_['Other']=other
            curriculum.append(Experience_)
            
            curriculum.append(Education_)
            curriculum.append(Other_)
            data['curriculum']=curriculum
            
            getPDF(data)

    return render(request, 'resume/resume_fill.html', {

        'personform': PersonForm(),
        'educationform': EducationForm(),
        'education2form': Education2Form(),
        'education3form': Education3Form(),
        'experienceform': ExperienceForm(),
        'experience2form': Experience2Form(),
        'experience3form': Experience3Form(),
        'otherform': OtherForm(),
        'infoform': InfoForm(),
        'contactform': ContactForm(),
        'letterform':LetterForm()
        
    })


