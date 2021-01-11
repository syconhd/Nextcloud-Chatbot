from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time

browser  = webdriver.Chrome(ChromeDriverManager().install())



username = "msfaya"
passwort = "r0000"

nachricht = "Hallo, ich bin anwesend"
sendezeitStunde = 7
sendezeitMinute = 24



#Sendeempfaenger (chat-URL)

Monday = "https://ncc.gymwm.de/call/ta45sknh" # zb: Herr Wolthius
Tuesday = ""
Wednesday = "https://ncc.gymwm.de/call/ta45sknh" 
Thursday= ""
Friday = ""
Saturday = "https://ncc.gymwm.de/call/qd65kx3i" # Akif Samstags
Sunday = "https://ncc.gymwm.de/call/sduaye5p"

empfaenger=""
x = datetime.datetime.now()
hour = int(x.strftime("%H"))
minute = int(x.strftime("%M"))

timez = ((sendezeitStunde-hour)*60*60) + ((sendezeitMinute-minute)*60)

if timez < 0:
	timez = 60*60*24+timez

print(timez)

if x.strftime("%A")=="Monday":
	empfaenger=Monday

elif x.strftime("%A")=="Tuesday":
	empfaenger=Tuesday

elif x.strftime("%A")=="Tuesday":
	empfaenger=Tuesday

elif x.strftime("%A")=="Wednesday":
	empfaenger=Wednesday

elif x.strftime("%A")=="Thursday":
	empfaenger=Thursday

elif x.strftime("%A")=="Saturday":
	empfaenger=Saturday

elif x.strftime("%A")=="Sunday":
	empfaenger=Sunday




def senden():
	print("john")
	# Website oeffnen
	browser.get('https://ncc.gymwm.de/apps/spreed/')

	#Benutzername und Passwort eingeben
	browser.find_element_by_name('user').send_keys(username)
	browser.find_element_by_name('password').send_keys(passwort)

	#Auf "Anmelden" clicken
	browser.find_element_by_id('submit-form').click();

	#Zu Empfaenger steuern und senden
	browser.get(empfaenger)
	browser.find_element_by_class_name('new-message-form__advancedinput').send_keys(nachricht)
	browser.find_element_by_css_selector('button.new-message-form__button.submit.icon-confirm-fade').click();
	

while True:
	
	time.sleep(timez)
	senden()

#cd C:\Users\User\Documents\Projekte\Desktop\Webbot 2.0