import gspread, json
from django.shortcuts import render
from oauth2client.service_account import ServiceAccountCredentials


context_dict = {}
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("C:\Users\DeLL\Downloads\Demo-7c819ff92803.json", scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1soBzI8ovNdMDeRO4BZW8VhYC86am5KraTK-IT1BgieY").sheet1

data = sheet.get_all_records()

excel_sheet = []
for i in data:
    excel_sheet.append(i['Email address'])
print excel_sheet        #[u'test@gmail.com', u'rt@gmail.com', u'ruhooo@gmail.com', u'XCV@gmail.com', u'aws@gmail.com', u'aps@gmail.com', u'uayvcyac@gmail.com']
