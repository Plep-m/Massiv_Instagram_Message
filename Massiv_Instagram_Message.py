#########################################################
################# Import libraries ######################
#########################################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import *
from selenium.webdriver.support import expected_conditions as EC
import time, random


#########################################################
################# Program functions #####################
#########################################################

#display massiv instagram message
def display():
	print("\n\n\n\n#########################################################################################")
	time.sleep(0.2)
	print("\n\n /$$      /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$ /$$    /$$	")
	time.sleep(0.1)
	print("| $$$    /$$$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/| $$   | $$	")
	time.sleep(0.1)
	print("| $$$$  /$$$$| $$  \ $$| $$  \__/| $$  \__/  | $$  | $$   | $$	")
	time.sleep(0.1)
	print("| $$ $$/$$ $$| $$$$$$$$|  $$$$$$ |  $$$$$$   | $$  |  $$ / $$/	")
	time.sleep(0.1)
	print("| $$  $$$| $$| $$__  $$ \____  $$ \____  $$  | $$   \  $$ $$/	")
	time.sleep(0.1)
	print("| $$\  $ | $$| $$  | $$ /$$  \ $$ /$$  \ $$  | $$    \  $$$/		")
	time.sleep(0.1)
	print("| $$ \/  | $$| $$  | $$|  $$$$$$/|  $$$$$$/ /$$$$$$   \  $/		")
	time.sleep(0.1)
	print("|__/     |__/|__/  |__/ \______/  \______/ |______/    \_/		")

	time.sleep(0.1)
	print("\n")
	time.sleep(0.1)
	print("\n")

	print(" /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$      /$$	")
	time.sleep(0.1)
	print("|_  $$_/| $$$ | $$ /$$__  $$|__  $$__//$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$$    /$$$	")
	time.sleep(0.1)
	print("  | $$  | $$$$| $$| $$  \__/   | $$  | $$  \ $$| $$  \__/| $$  \ $$| $$  \ $$| $$$$  /$$$$	")
	time.sleep(0.1)
	print("  | $$  | $$ $$ $$|  $$$$$$    | $$  | $$$$$$$$| $$ /$$$$| $$$$$$$/| $$$$$$$$| $$ $$/$$ $$	")
	time.sleep(0.1)
	print("  | $$  | $$  $$$$ \____  $$   | $$  | $$__  $$| $$|_  $$| $$__  $$| $$__  $$| $$  $$$| $$	")
	time.sleep(0.1)
	print("  | $$  | $$\  $$$ /$$  \ $$   | $$  | $$  | $$| $$  \ $$| $$  \ $$| $$  | $$| $$\  $ | $$	")
	time.sleep(0.1)
	print(" /$$$$$$| $$ \  $$|  $$$$$$/   | $$  | $$  | $$|  $$$$$$/| $$  | $$| $$  | $$| $$ \/  | $$	")
	time.sleep(0.1)
	print("|______/|__/  \__/ \______/    |__/  |__/  |__/ \______/ |__/  |__/|__/  |__/|__/     |__/	")

	time.sleep(0.1)
	print("\n")
	time.sleep(0.1)
	print("\n")

	print(" /$$      /$$ /$$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$	")
	time.sleep(0.1)
	print("| $$$    /$$$| $$_____/ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$| $$_____/	")
	time.sleep(0.1)
	print("| $$$$  /$$$$| $$      | $$  \__/| $$  \__/| $$  \ $$| $$  \__/| $$			")
	time.sleep(0.1)
	print("| $$ $$/$$ $$| $$$$$   |  $$$$$$ |  $$$$$$ | $$$$$$$$| $$ /$$$$| $$$$$		")
	time.sleep(0.1)
	print("| $$  $$$| $$| $$__/    \____  $$ \____  $$| $$__  $$| $$|_  $$| $$__/		")
	time.sleep(0.1)
	print("| $$\  $ | $$| $$       /$$  \ $$ /$$  \ $$| $$  | $$| $$  \ $$| $$			")
	time.sleep(0.1)
	print("| $$ \/  | $$| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$$	")
	time.sleep(0.1)
	print("|__/     |__/|________/ \______/  \______/ |__/  |__/ \______/ |________/	")

	time.sleep(0.1)
	print("\n")
	time.sleep(0.1)
	print("\n")

	print("#########################################################################################")
	time.sleep(0.1)
	print("\n\n")


#connection à instagram :
def auth(my_username, my_password, time_actions, browser):
	try:
		print("\n\n#################################################\n\n")
		print("Connection to instagram... [may take a while]")
		#connection to instagram.com
		print("(Connection to instagram.com...)")
		browser.get('https://instagram.com')
		time.sleep(random.randrange(time_actions+3, time_actions+5))


		#click on "only allow essential cookies"
		print("(click on \"only allow essential cookies\")")
		browser.find_element_by_xpath(".//button[@class='aOOlW   HoLwm ']").click()
		time.sleep(random.randrange(time_actions, time_actions +2))

		#connection with your account
		print("(connection with your account)")
		input_username = browser.find_element_by_name('username')
		input_password = browser.find_element_by_name('password')
		input_username.send_keys(my_username)
		time.sleep(random.randrange(0, 2))
		input_password.send_keys(my_password)
		time.sleep(random.randrange(0, 2))
		input_password.send_keys(Keys.ENTER)
		time.sleep(random.randrange(time_actions+3, time_actions+5))

		#click on "Not Now" to save informations
		browser.find_element_by_xpath(".//button[@class='sqdOP yWX7d    y3zKF     ']").click()
		print("(connection with your account)")
		time.sleep(random.randrange(time_actions, time_actions+2))

		# click on "Not Now" to turn on notifications
		print("(click on \"Not Now\" to turn on notifications)")
		browser.find_element_by_xpath(".//button[@class='aOOlW   HoLwm ']").click()
		time.sleep(random.randrange(time_actions, time_actions +2))

		print("\n\n#################################################\n\n")
		print("start of message sendding...")


	#display the error if there is one
	except Exception as err:
		print(err)
		browser.quit()


#send messages :
def send_message(usernames, message, time_actions, number_users):
	try:

		#calcul of datas
		i=0
		temps_base = 6 * (time_actions) * number_users

		#send to all users
		for user in usernames:

			#caclculs for time
			i += 1
			pourcentage = 100 * i / number_users
			temps_base = 6 * (time_actions) * (number_users - i)

			if temps_base / 3600 > 1:
				temps_heure = int(temps_base / 3600)
				temps_minute = int((temps_base - temps_heure * 3600) / 60)
				temps_final = ""
				temps_final = str(temps_heure) + " Ours " + str(temps_minute) + " Minutes "

			elif (temps_base / 3600) < 1 and (temps_base / 60) > 1:
				temps_minute = int(temps_base / 60)
				temps_final = ""
				temps_final = str(temps_minute) + " Minutes "

			else:
				temps_seconde = (temps_base)
				temps_final = ""
				temps_final = "A few seconds..."

			#display of progression,
			print("\n\n\n\n")
			print("########################")
			print("\n\n Progression  \n\n ", int(pourcentage), " %\n\n")
			print("########################")
			print("\n\n User  \n\n [", i, "/", number_users, "]\n\n")
			print("########################")
			print("\n\n Remaining time \n\n ", temps_final, "\n\n")
			print("########################")
			print("\n\n current user  \n\n", user, "\n\n")
			print("######################## \n\n")
			time.sleep(random.randrange(time_actions, time_actions+2))

			#search for the current user
			browser.find_element_by_xpath("//input[@placeholder='Search']").send_keys(user)
			time.sleep(random.randrange(time_actions+3, time_actions+5))

			#click to his profil
			browser.find_element_by_class_name('-qQT3').click()
			time.sleep(random.randrange(time_actions, time_actions+1))

			#click on the button message
			browser.find_element_by_xpath(".//button[@class='sqdOP  L3NKy    _8A5w5    ']").click()
			time.sleep(random.randrange(time_actions, time_actions+2))

			#search the field to send the message
			text_area = browser.find_element_by_xpath("//textarea[@placeholder='Message...']")
			time.sleep(random.randrange(time_actions, time_actions-2))

			#tip the message
			text_area.send_keys(messages)
			time.sleep(random.randrange(time_actions, time_actions-2))

			#send the message
			text_area.send_keys(Keys.ENTER)
			time.sleep(random.randrange(time_actions, time_actions+2))

	# display the error if there is one
	except Exception as err:
		print(err)
		browser.quit()








#########################################################
################### Main Programm #######################
#########################################################

#display
display()

#your account :
my_username = str(input('Your username account \n\n > \a'))
print("\n\n#################################################\n\n")
my_password = str(input('Your passworld account \n\n > \a'))

#users (you must follow them) :
username = []
number_users=0
file = open("users.txt", "r")
all = file.readlines()
for car in all:
	number_users+=1
	username.append(car)


#time between actions :
print("\n\n#################################################\n\n")
time_actions=str(input("Do you use a VPN or something that\ncan slow down your browser ? \n[Y/N] \n\n > \a"))
if time_actions.upper()=="Y":
	time_actions=7
else:
	time_actions=4

#Messages to send :
print("\n\n#################################################\n\n")
message = str(input("What is the message to send ? \n\n > \a"))


#strat the browser :
print("\n\n#################################################\n\n")
print("Start of the browser...")
browser = webdriver.Chrome('chromedriver')


#conection to instagram et send of the message :

auth(my_username, my_password,time_actions, browser)
send_message(username, message, time_actions, number_users)
display()


