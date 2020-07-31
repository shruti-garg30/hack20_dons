import gspread
import webbrowser
import requests
import re 
def callfunction(ans_list):
    def remove_till_at(the_list):
        a=[]
        for y in the_list:
            a.append(y.split('@'))
        b=[]
        for x in a:
            b.append(x[1])
        b1= 'http://'
        b1 += '{0}'
        b= [b1.format(i) for i in b]
        return b
    for x in ans_list:
        if '@hevo' in x:
            ans_list.remove(x)
    c= remove_till_at(ans_list)
    print(c)
    for x in c:
       webbrowser.open_new_tab(x)
