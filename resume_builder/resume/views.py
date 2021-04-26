from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.sites.requests import RequestSite
from .utils import getPDF
import cv2
from django.conf import settings
import numpy as np
from PIL import Image

from .models import Person, Education, Experience, Other, contact, personal_info
from .forms import PersonForm, EducationForm, ExperienceForm, OtherForm, ContactForm, InfoForm,LetterForm


def resumeFill(request):
    if request.method == 'POST':
        personform = PersonForm(request.POST,request.FILES)
        educationform = EducationForm(request.POST)
        experienceform = ExperienceForm(request.POST)
        otherform = OtherForm(request.POST)
        infoform = InfoForm(request.POST)
        contactform = ContactForm(request.POST)
        letterform = LetterForm(request.POST,request.FILES)
        
        print(bool(request.FILES))

      
            
       
        if personform.is_valid() and bool(request.FILES):
            
            
            filename = personform.cleaned_data['picture']
            pil_img = Image.open(filename).convert('RGB')
            cv_img = np.array(pil_img)
            cv2.imwrite(settings.MEDIA_ROOT+'/photo.jpg',cv_img[:,:,::-1])
            personform.cleaned_data['picture']='photo.jpg'
            
            
        '''
        if educationform.is_valid():
            #educationform.save()
            print('education',educationform.cleaned_data)
            
        if experienceform.is_valid():
            #experienceform.save()
            print('experience',experienceform.cleaned_data)
            
        if otherform.is_valid():
            #otherform.save()
            print('other',otherform.cleaned_data)
            
        if infoform.is_valid():
            #infoform.save()
            print('info',infoform.cleaned_data)
                
        if contactform.is_valid():
            #contactform.save()
            print('contact',contactform.cleaned_data)'''
        if letterform.is_valid() and bool(request.FILES):
            filename = letterform.cleaned_data['stamp']
            pil_img = Image.open(filename).convert('RGB')
            cv_img = np.array(pil_img)
            
            cv2.imwrite(settings.MEDIA_ROOT+'/stamp.jpg',cv_img[:,:,::-1])
            letterform.cleaned_data['stamp']='stamp.jpg'
            
        if (
            educationform.is_valid() and personform.is_valid() 
            and experienceform.is_valid() and otherform.is_valid() 
            and infoform.is_valid() and contactform.is_valid() 
            and letterform.is_valid()
             ):
            print('valid')
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
                  'title':experienceform.cleaned_data['company'],
                  'subtitle':experienceform.cleaned_data['job_title'],
                  'detail':experienceform.cleaned_data['job_detail'],
                  'description':experienceform.cleaned_data['job_description'], 
                  'highlight':True,
                  'date': f"{experienceform.cleaned_data['start_Date'].year}-{experienceform.cleaned_data['end_Date'].year}"
                },
                {
                  'title':experienceform.cleaned_data['company'],
                  'subtitle':experienceform.cleaned_data['job_title'],
                  'detail':experienceform.cleaned_data['job_detail'],
                  'description':experienceform.cleaned_data['job_description'], 
                  'highlight':True,
                  'date': f"{experienceform.cleaned_data['start_Date'].year}-{experienceform.cleaned_data['end_Date'].year}"
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
                  'title':educationform.cleaned_data['institution'],
                  'subtitle':educationform.cleaned_data['level'],
                  'detail':educationform.cleaned_data['detail'],
                  'description':educationform.cleaned_data['description'], 
                  'highlight':True,
                  'date': f"{educationform.cleaned_data['start_date'].year}-{educationform.cleaned_data['end_date'].year}"
                },
                {
                  'title':educationform.cleaned_data['institution'],
                  'subtitle':educationform.cleaned_data['level'],
                  'detail':educationform.cleaned_data['detail'],
                  'description':educationform.cleaned_data['description'], 
                  'highlight':True,
                  'date': f"{educationform.cleaned_data['start_date'].year}-{educationform.cleaned_data['end_date'].year}"
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
        'experienceform': ExperienceForm(),
        'otherform': OtherForm(),
        'infoform': InfoForm(),
        'contactform': ContactForm(),
        'letterform':LetterForm()
        
    })


