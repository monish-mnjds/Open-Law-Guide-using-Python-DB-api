import webbrowser
from PIL import Image
import pywhatkit as kit
import smtplib
import secrets
import credentials as cr
import time
import mysql.connector
mydb = mysql.connector.Connect(host = "127.0.0.1", user = "root", password = "enter ur password", database = 'enter ur database')
class Admin():
    def login(self):
        mycursor = mydb.cursor()
        mycursor.execute('Select * from password1;')
        result = mycursor.fetchone()
        usern = input('\nUsername: ')
        passw = input('\nPassword: ')
        if result[1] == passw and result[0] == usern:
            print('\n\n-----Welcome Admin-----\n')
            a.edit()
        else:
            print('\nRetry...\n')
            a.login()
    def deleting(self):
        mycursor = mydb.cursor()
        s = 'delete from lawyers where lawyername='
        s1 = input("\nEnter the lawyer's name to delete his/her record: ")
        s2 = s+"'"+s1+"'"
        mycursor.execute(s2)
        mydb.commit()
        time.sleep(0.5)
        print('\nRecord Deleted...')
    def inserting(self):
        l = []
        print('\nEnter in this format-->\t1)lawyername 2)expertise 3)phone 4)fees: ')
        inc = 1
        while inc <= 4:
            into = input('\nPopulate Data : ')
            l.append(into)
            inc += 1
        value = tuple(l)
        mycursor = mydb.cursor()
        query = "insert into lawyers (lawyername, expertise, phone, fees) values(%s, %s, %s, %s)"
        mycursor.execute(query,value)
        mydb.commit()
        time.sleep(0.75)
        print('\nRecord Inserted...')
    def changepassword(self):
        mycursor = mydb.cursor()
        s = 'update password1 set passcode='
        s1 = " where Username='monish';"
        s2 = input("\nEnter the new password: ")
        s3 = s+"'"+s2+"'"+s1
        mycursor.execute(s3)
        mydb.commit()
        time.sleep(0.75)
        print('\nPassword Changed...')
class Change(Admin):
    def edit(self):
        print("Press   A for Inserting\n\tB for Deleting\n\tC for changing password\n\tE for exit")
        while True:
            opt = input('\nYour option: ')
            if opt == 'b' or opt == 'B':
                print('\n----Delete Details----')
                a.deleting()
                continue
            elif opt == 'a' or opt == 'A':
                print('\n----Insert Details----')
                a.inserting()
                continue
            elif opt == 'c' or opt == 'C':
                print('\n----Change password----')
                a.changepassword()
                continue
            elif opt == 'e' or opt == 'E':
                print('\n-----MAIN MENU-----')
                break
            else:
                print('\nEnter A, B, C (or) E')
                continue
    def userlogin(self):
        while True:
            def send_mail(subject,otp):
                try:    
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(cr.email1,cr.password)
                    OTP = 'Subject: {}\n\n{}'.format(subject,otp)
                    cr.email2 = input('\nEnter ur email id : ')
                    server.sendmail(cr.email1,cr.email2,OTP)
                    server.quit()
                    print("\nEmail has been sent...")
                except:
                    print('\nEmail failed to send....')
            subject = 'One-Time Password...'
            truth = secrets.SystemRandom()
            otp = str(truth.randrange(100000,999999))
            msg = 'Your One Time Password is : ' + otp
            send_mail(subject,msg)
            otpmail = input('\nEnter the 6 digit OTP : ')
            if otpmail == otp:
                a.law()
            else:
                print('\nOTP may be wrong')
                toredo = input("\nTo Retry Press 'R' or E to exit: ")
                if toredo == 'r' or toredo == 'R':
                    continue
            break
class Detail(Change):
    def highcourts(self):
        file_format = 'High_courts_of_India.png'
        im = Image.open(file_format)
        im.show()
    def googlesearch(self):
        search_item = input('\nEnter what you want to search : ')
        kit.search(search_item)
    def ecourts(self):
        webbrowser.open('https://districts.ecourts.gov.in/vellore')
    def news(self):
        webbrowser.open('https://www.pib.gov.in/')
    def lawmin(self):
        webbrowser.open('http://lawmin.gov.in/') 
    def casa(self):
        webbrowser.open('https://www.indiacode.nic.in/')
    def sci(self):
        webbrowser.open('https://main.sci.gov.in/')
    def par(self):
        webbrowser.open('https://www.prsindia.org/')
    def listing(self):
        mycursor = mydb.cursor()
        mycursor.execute('select * from lawyers')
        result = mycursor.fetchall()
        for i in result:
            print('\nName: ',i[0])
            print('Expertise: ',i[1])
            print('Phone: ',i[2])
            print('Fees: ',i[3])
class Personal(Detail):
    def menu(self):
        print('''\nPress   A for QR Code of High courts
        B for Google Search
        C for E-Courts
        D for Govt.News(PIB)
        E for exit
        F for LAW Ministry Website
        G for Central and State Acts
        H for Supreme of India
        I for Parliamentary updates(PRS)
        J for List of lawyers''')
    def law(self):
        while True:
            a.menu()
            opt = input('\nYour option: ')
            if opt == 'a' or opt == 'A':
                print('\n----QR code----')
                a.highcourts()
                continue
            elif opt == 'b' or opt == 'B':
                print('\n----Google Search----')
                a.googlesearch()
                continue
            elif opt == 'c' or opt == 'C':
                print('\n----E-Courts----')
                a.ecourts()
                continue
            elif opt == 'd' or opt == 'D':
                print('\n----Govt news----')
                a.news()
                continue
            elif opt == 'f' or opt == 'F':
                print('\n----Law ministry website----')
                a.lawmin()
                continue
            elif opt == 'G' or opt == 'g':
                print('\n----Central and state acts----')
                a.casa()
                continue
            elif opt == 'H' or opt == 'h':
                print('\n----Supreme Court of India website----')
                a.sci()
                continue
            elif opt == 'i' or opt == 'I':
                print('\n----Parliamentary updates----')
                a.par()
                continue
            elif opt == 'j' or opt == 'J':
                print('\n----List of Lawyers----')
                a.listing()
                continue
            elif opt == 'e' or opt == 'E':
                print('\n-----MAIN MENU-----')
                break
            else:
                print('\nEnter Valid option (or) E')
                continue

a = Personal()
print('\n\t-----WELCOME TO LAW SITE-----')

if __name__ == '__main__':
    while 1:
        i = input("\n1 for Admin\n2 for User\nE/e for Exit\n-----> ")
        if i == '1':
            a.login()
            continue
        elif i == '2':
            a.userlogin()
            continue
        elif i == 'e' or i == 'E':
            print('\n---BYE!!!---')
            break
        else:
            print('\nPLEASE ENTER 1,2 (or) E')
            continue       
