from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class employee(models.Model):
    timestamp = models.CharField(max_length=200)
    email_address = models.EmailField(primary_key=True, max_length=254)
    name = models.CharField(max_length=200)
    current_city = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=50)
    age = models.CharField(max_length=120)
    current_or_last_employer = models.CharField(max_length=200)                           #If_you're_a_fresher,please_mention_NA
    job_role = models.CharField(max_length=200)
    current_or_last_CTC = models.CharField(max_length=200)                      #If you 're a fresher, please mention NA.
    FIXED_component_CTC = models.CharField(max_length=200)
    work_experience = models.CharField(max_length=200)                           #IN MONTHS)
    days_working_in_a_week = models.CharField(max_length=200)
    relocate_to_Mumbai = models.CharField(max_length=200)              #(This job role is for Mumbai location. If onboarded, you'll be working from home initially, but once the current situation due to Covid settles down, you'll have to relocate to Mumbai)
    english_communication= models.CharField(max_length=11)                     #(1-10)
    skills = models.CharField(max_length=200)                           #If_you're_a_fresher,please_mention_NA
    previous_industries = models.CharField(max_length=200)
    post_sale_profile = models.CharField(max_length=200)                                 #What kind of profile would you like to work in after working in Sales/Business development
    select = models.CharField(max_length=200)                                 #Select the 3 factors out of the following that matter the most to you while selecting a job?
    upload_resume = models.CharField(max_length=200)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.email_address

