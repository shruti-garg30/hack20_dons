import gspread
import webbrowser
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
#scope = ['https://spreadsheets.google.com/feeds']
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("email sample").sheet1

# Extract and print all of the values
email_list = sheet.get_all_values()
#print (list_of_hashes)
def remove_till_at(the_list):
    a=[]
    for x in the_list:
        for y in x:
            a.append(y.split('@'))
    b=[]
    for x in a:
        b.append(x[1])
    b1= 'http://'
    b1 += '{0}'
    b= [b1.format(i) for i in b]
    return b
c= remove_till_at(email_list)
#print(c[:5])
for x in c:
    webbrowser.open_new_tab(x)
