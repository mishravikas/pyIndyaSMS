#Indyarocks SMS sender
#Keywords python free sms api
#Author Vikas Mishra<vikasmishra95@gmail.com>
#Dependicies : Twill
#It can be installed from here : http://twill.idyll.org/
#Sent messages will be saved in a text file named "smslog.txt".


import getpass #to take  password input without displaying it on screen
import os
from twill.commands import *
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--about", 
                    version="""
                    pyIndyasms V1.01 command line SMS sender
                    By
                    Vikas Mishra
                    <vikasmishra95@gmail.com>

                    """,action='version')    

    
args = parser.parse_args()



username=raw_input("Enter indyarocks username: ")
password=getpass.getpass("Enter password: ")

def sendSMS():
        try:

                go("http://www.indyarocks.com")
                fv("1","LoginForm[username]",username)
                fv("1","LoginForm[password]",password)
                submit()
        except:
                print "Sorry this API needs updation contact "
        
        number=raw_input("Enter to number : ")
        message=raw_input("Enter message to %s: " %(number))
        try:
                go("http://www.indyarocks.com/send-free-sms")
                fv("3","FreeSms[mobile]",number)
                fv("3","FreeSms[post_message]",message)
                submit()
                os.system("echo Time : `date` >> mysmslog.txt")        
                os.system("echo Number : %s >> mysmslog.txt" %number)
                os.system("echo Message : %s >> mysmslog.txt" %message)
                os.system("echo ---------------------------------------------------------------- >> mysmslog.txt")
                print "Successfully sent"
        except:
                print "Username and password did not match"

     
sendSMS()
                
