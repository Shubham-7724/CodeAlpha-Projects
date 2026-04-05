# Task Automation with Python Scripts 
# This program extracts all the email addresses from a .txt file and saves them to another file. 


import os 
import re

with open("messy_employee_records.txt" , 'r') as F:                      #opening the existing txt file
    R1 = F.read()

    pattern = re.compile(r'[a-zA-Z0-9._]+@[a-z]+\.(com|org|net|in)')     #making the format of the email addresses

    matches = pattern.finditer(R1)

    for match in matches:
        print(match.group())

        with open("new_emails_file.txt" , 'a+') as T:                    
            R2 = T.writelines(match.group() + "\n")                      #adding the email addresses to another file



    

