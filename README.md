"""Problem
A number N will be given as input, followed by N email addresses. Few of the email address might be wrong, the output should contain valid email addresses.Sample Input hello@example username@domain.com her323@#89asdf.fds
Sample Output username@domain.com """

PROGRAM
import re
num=int(input("Enter number:"))
for  i in range(num):
    emails=input()
    email = re.findall(r'[\w\.-]+@[\w\.-]+',emails)
    for emails in email:
            print(emails) 
