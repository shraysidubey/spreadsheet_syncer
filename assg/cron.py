import gspread
from oauth2client.service_account import ServiceAccountCredentials
from assg.models import employee
from django_cron import CronJobBase, Schedule
import os

class PushCronJob(CronJobBase):

    RUN_EVERY_MINS = 1                                         #every 1 min

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = "my_app.super_awesome_push_cron"                    #a unique code

    def do(self):

        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        DIRNAME = os.path.dirname(__file__)

        creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(DIRNAME, 'google_api_key.json'),scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_key("1soBzI8ovNdMDeRO4BZW8VhYC86am5KraTK-IT1BgieY").sheet1
        data = sheet.get_all_records()                          #[{}, {}, {}, {}]

        excel_sheet = []
        for i in data:
            excel_sheet.append(i['Email address'])
        #print excel_sheet                    #[u'test@gmail.com', u'rt@gmail.com', u'ruhooo@gmail.com', u'XCV@gmail.com', u'aws@gmail.com', u'aps@gmail.com', u'uayvcyac@gmail.com']

        database = []
        emplyee_profiles = employee.objects.all()
        for employee_profile in emplyee_profiles:
            database.append(employee_profile.email_address)
        #print "L", database            #['test@gmail.com', 'rt@gmail.com', 'ruhooo@gmail.com]

        records_to_be_deleted = []
        for i in database:
            if i not in excel_sheet:
                records_to_be_deleted.append(i)

        employee.objects.filter(email_address__in=records_to_be_deleted).delete()

        for i in data:

            S = employee()
            S.timestamp = data[0]['Timestamp']
            S.email_address = i['Email address']
            S.name = i['What is your name?']
            S.current_city = i['Your current city?']
            S.contact_number = i['Your contact number?']
            S.age = i['Your age?']
            S.current_or_last_employer = i['Please mention the name of your most recent company (current/ last employer).If you are a fresher, please mention NA']
            S.job_role = i['Whats your job role in your current/ last company?']
            S.current_or_last_CTC = i['What is your current/ last drawn CTC? If you are a fresher, please mention NA.']
            S.FIXED_component_CTC = i['What is/ was the FIXED component in your CTC? If you are a fresher, please mention NA.']
            S.work_experience = i['(IN MONTHS) What is your total work experience?']
            S.days_working_in_a_week = i['Are you comfortable working 6 days a week (with a weekday off)?']
            S.relocate_to_Mumbai = i['Are you willing to relocate to Mumbai? (This job role is for Mumbai location. If onboarded, you will be working from home initially, but once the current situation due to Covid settles down, you will have to relocate to Mumbai)']
            S.english_communication = i['On a scale of 1-10, How do you rate yourself on your verbal english communication skills']
            S.skills = i['Which of the following skills you have worked in (atleast 6 months)']
            S.previous_industries = i['Which of the following industries you have worked in?']
            S.post_sale_profile = i['What kind of profile would you like to work in after working in Sales/Business development?']
            S.select = i['Select the 3 factors out of the following that matter the most to you while selecting a job?']
            S.upload_resume = i['Please upload your latest resume']
            S.save()