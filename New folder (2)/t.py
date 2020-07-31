import gspread
import webbrowser
import requests
import re 
from oauth2client.service_account import ServiceAccountCredentials
from validate_email import validate_email
def check():
    scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("email sample").sheet1

    # Extract and print all of the values
    email_list = sheet.get_all_values()
    list_validate=[]
    list_invalidate=[]
    hevo='@hevo'
    for x in email_list:
        if '@hevo' in x[0]:
            #list_invalidate.append(x[0])
            email_list.remove(x)
    for x in email_list:
        try:
            is_valid = validate_email(email_address=x[0], check_regex=True, check_mx=True, from_address='my@from.addr.ess', helo_host='my.host.name', smtp_timeout=20, dns_timeout=20, use_blacklist=True, debug=False)
            if(is_valid==True):
                list_validate.append(x[0])
            else:
                list_invalidate.append(x[0])
        except:
            list_invalidate.append(x[0])
    

    return list_invalidate

