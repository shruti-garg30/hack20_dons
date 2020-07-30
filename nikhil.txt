import webbrowser
from csv import reader

the_file = 'C:/Users/Master/Desktop/hevothon/emails.csv'
opened_file= open(the_file)

email_list= list(reader(opened_file))
#print(email_list[:5])
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
