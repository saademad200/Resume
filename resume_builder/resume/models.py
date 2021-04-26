from __future__ import unicode_literals
from django_countries.fields import CountryField
from django.db import models
from django import forms

class Person(models.Model):
    picture = models.ImageField(default='template_photo.JPG', upload_to='profile_pics')
    name = models.CharField(max_length=255,default='')
    occupation = models.CharField(max_length=255,default='')
    about_Me = models.TextField(default='')


class Education(models.Model):
   
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    detail = models.CharField(max_length=255,default='')
    institution = models.CharField(max_length=255,default='')
    level = models.CharField(max_length=255,default='')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(default='')


class Experience(models.Model):
                   
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    job_detail = models.CharField(max_length=255,default='')
    company = models.CharField(max_length=255,default='')
    job_title = models.CharField(max_length=255,default='')
    start_Date = models.DateField(blank=True, null=True)
    end_Date = models.DateField(blank=True, null=True)
    job_description = models.TextField(default='')


class contact(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE,default='')
    email = models.EmailField(max_length = 150,default='')
    address = models.TextField( max_length = 2000,default='')
    phone = models.CharField(max_length=255,default='')
    website = models.URLField(max_length=250,default='')

class personal_info(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    nationality = CountryField(blank_label='(select country)')
    residency = models.CharField(max_length=255,default='')
    languages = models.CharField(max_length=255,help_text="Enter Comma Seperated Values") 


class Other(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    extra_detail = models.CharField(max_length=255,default='')
    extra_title = models.CharField(max_length=255,default='')
    extra_subtitle = models.CharField(max_length=255,default='')
    startDate = models.DateField(blank=True, null=True)
    endDate = models.DateField(blank=True, null=True)
    extra_description = models.TextField(default='')

class Letter(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    author = models.CharField(max_length=255,default='')
    stamp = models.ImageField(default='template_signature.png', upload_to='stamp')
    recepient = models.CharField(max_length=255,default='')
    formulation = models.CharField(max_length=255,default='')
    text = models.TextField(default='')
    date = models.DateField(blank=True, null=True)

