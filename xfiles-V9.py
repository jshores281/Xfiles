#!/bin/python3

import os, sys, time, smtplib
import datetime
from datetime import date
from shutil import copy2



ct = datetime.datetime.now()
cur_time = ct.strftime("%H:%M:%S")
today = date.today()
d1 = today.strftime("%m/%d/%Y")


# generator GET loop
def fold_mon(src_folder):
	cntr = 1
	static_dir = os.listdir(credz.src_folder)
	new_Dir = []
	sDircount = len(static_dir)
	dDircount = len(new_Dir)
	bytesize = sys.getsizeof(credz.fmon)
#UPDATE loop
	while True:						
		bytesize = sys.getsizeof(credz.fmon)
		#time.sleep(1)
		live_dir = os.listdir(credz.src_folder)
		new_Dir = []
		lDircount = len(live_dir)
#--ADDS NEW ELEMENTS TO NEW LIST
		add_Dir = [item for item in live_dir if item not in static_dir]
# ADD SUBTRACTED ELEMENTS TO NEW LIST
		sub_Dir = [item for item in static_dir if item not in live_dir]		
		new_Dir = add_Dir + sub_Dir
		dDircount = len(new_Dir)
		yield bytesize, cntr, static_dir, live_dir, new_Dir, add_Dir, sub_Dir, lDircount, sDircount, dDircount  
# UPDATES STATIC LIST EVERY EVEN ITERATION
		if cntr % 2:
			print("STATIC LIST STATUS: *UPDATED*")								
			print('\n',">> items added to folder %s" % add_Dir,'\n',">> items removed from folder %s" % sub_Dir)
			static_dir = os.listdir(credz.src_folder)
			sDircount = len(static_dir)
			time.sleep(1)
# UPDATES STATIC LIST EVERY ODD ITERATION
		if not cntr % 2:
			print("STATIC LIST STATUS: *STATIC*")								
			print('\n', ">> items added to folder %s" % add_Dir,'\n',">> items removed from folder %s" % sub_Dir)
			static_dir = os.listdir(credz.src_folder)
			sDircount = len(static_dir)
			time.sleep(1)
		cntr += 1








# CONFIRMATION loop
def fold_run():							
	for bytesize, cntr, static_dir, live_dir, new_Dir, add_Dir, sub_Dir, lDircount, sDircount, dDircount in credz.fmon:
		print('\n'
			,'--------------------------------------------------------------------------', '\n'
			,'--------------------------------------------------------------------------', '\n'
			,"this loop is %s bytes" % bytesize, '\n'
			,"this loop is a: ", type(credz.fmon),'\n'
			,"this loop is on count: %s" % cntr, '\n'
			,'--------------------------------------------------------------------------', '\n'
			,"----SRC-FOLDER LOCATION----",'\n','>>',credz.src_folder, '\n'
			,'--------------------------------------------------------------------------', '\n'*2
			,"----SRC-FOLDER CONTENTS----",'\n'
			,'>>',"%s ITEMS in SRCfolder ~ "% lDircount, live_dir,'\n','\n'

			,"----STATIC-FOLDER CONTENTS----",'\n'
			,'>>',"%s ITEMS in STCfolder ~ "% sDircount, static_dir,'\n'
			,'--------------------------------------------------------------------------', '\n'*2

			,"----DST-FOLDER CONTENTS----",'\n'
			,'>>',"%s ITEMS in DSTfolder ~ "% dDircount, new_Dir, '\n'
			,'--------------------------------------------------------------------------'
			,'\n', '\n', '\n', '\n', sep=' ', end='', flush=True)	
		
# PACKAGE ACTION ON TRIGGER HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		if dDircount > 0:

			ct = datetime.datetime.now()
			cur_time = ct.strftime("%H:%M:%S")
			today = date.today()
			d1 = today.strftime("%m/%d/%Y")

			#print(f" {d1}{cur_time} ")
			#time.sleep(1)
			
			#print(main_menu.MENU_CHOICE)
			confadd_dir = ">>items added to folder::%s" % add_Dir
			confsub_dir = ">>items removed from folder::%s" % sub_Dir

			logger = confadd_dir, confsub_dir

			if main_menu.MENU_CHOICE=="1":
				with open(log_alert.dst_folder, "a") as file:
					file.write(f"\n::[{d1}]::[{cur_time}]{confadd_dir}{confsub_dir}")

			if main_menu.MENU_CHOICE=="2":				
				print("--------------------------------------------------------------------------",'\n'
				,"**SENDING ALERT TO**\n%s \n%s \n%s" % (credz.RECV_ADDR,confadd_dir,confsub_dir),'\n'
				,"--------------------------------------------------------------------------",'\n')
			
				SUBJECT = str("XFILES_MONITORING:\n\n")
				BODY = str(credz.src_folder + confadd_dir + confsub_dir)
				notify_user(credz.EMAIL_ADDR, credz.EMAIL_PASS, credz.EMAIL_SRVR, credz.EMAIL_PORT, credz.RECV_ADDR, SUBJECT, BODY)




def event_log():
	credz.src_folder = input("copy folder path here: ")
	#dstfolder = input("copy destination folder path here: ")=
	credz.fmon = fold_mon(credz.src_folder)
	# RUN FUNCTION
	fold_run()




def credz():
	EMAIL_SENDER = input("EMAIL: ")
	EMAIL_PASSWORD = input("PASSWORD: ")
	EMAIL_SRVR = input("SMTP SERVER: ")
	EMAIL_PORT = input("SMTP SERVER PORT: ")
	RECV_PHONE = input("CELL PHONE: ")
	SMS_GATE = input("CARRIER SMS-GATEWAY: ")

	credz.EMAIL_ADDR = EMAIL_SENDER
	credz.EMAIL_PASS = EMAIL_PASSWORD
	credz.EMAIL_SRVR = EMAIL_SRVR
	credz.EMAIL_PORT = EMAIL_PORT
	credz.RECV_ADDR = RECV_PHONE + SMS_GATE

	print("\n",
		"EMAIL = %s" % credz.EMAIL_ADDR,"\n",
		"PASSWORD = %s" % credz.EMAIL_PASS,"\n",
		"SERVER = %s" % credz.EMAIL_SRVR,"\n",
		"PORT = %s" % credz.EMAIL_PORT,"\n",
		"PHONE & SMS-GATEWAY = %s" % credz.RECV_ADDR,"\n")
	cred_correct = input("INFO CORRECT: [Y] / [N] > ")
	cred_correct = cred_correct.upper()
	if cred_correct == "N":
		credz()
	if cred_correct == "Y":
		print("\n"*2)
		# GLOBAL VARIABLES
		credz.src_folder = input("copy folder path here: ")
		#dstfolder = input("copy destination folder path here: ")
		credz.fmon = fold_mon(credz.src_folder)
		# RUN FUNCTION
		fold_run()

		

def log_alert():


	credz.src_folder = input("copy folder path here: ")
	log_file = input("log file name: ")
	log_alert.dst_folder = os.path.join(os.getcwd(), log_file)
	#log_alert.dst_folder = os.path.dirname(os.getcwd())
	#log_alert.dst_folder = log_alert.dst_folder.join(log_file)
	print(log_alert.dst_folder)
	
	#log_alert.dst_folder = input("copy log destination path here: ")
	credz.fmon = fold_mon(credz.src_folder)
	fold_run()


# email to sms function
def notify_user(EMAIL_ADDR, EMAIL_PASS, EMAIL_SRVR, EMAIL_PORT, RECV_ADDR, SUBJECT, BODY):
	with smtplib.SMTP(credz.EMAIL_SRVR, credz.EMAIL_PORT) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(credz.EMAIL_ADDR, credz.EMAIL_PASS)
		login_log = smtp.login(credz.EMAIL_ADDR, credz.EMAIL_PASS)
		print("SERVER LOGIN RESPONSE: ",'\n',login_log)
		
# make this reprogrammable based on product and values
		subject = SUBJECT
		body = BODY
# email message packer
		MSG = ("From: %s\r\n" % credz.EMAIL_ADDR
             + "To: %s\r\n" % credz.RECV_ADDR
             + "Subject: %s\r\n" % subject
             + "\r\n"
             + body)
		smtp.sendmail(credz.EMAIL_ADDR, credz.RECV_ADDR, MSG)
		print("\nSENDING EMAIL\n")
		time.sleep(1)







def main_menu():
	# GLOBAL VARIABLES
	if sys.platform == 'linux' or sys.platform == 'linux2':
		os.system('clear')
	elif sys.platform == 'win32':
		os.system("cls")
		os.system("title ~~~~OS FOLDER MONITORING SYSTEM~~~~")
	while True:
		print("""
-----------------------------------------
-----  OS FOLDER MONITORING SYSTEM  -----
-----------------------------------------
----------- ALERT OPTIONS ---------------
-----------------------------------------

[1] - FILE LOGGING = Logs changes of a directory to a log.txt file

[2] - EMAIL/SMS-GATEWAY ALERTS = Send message when folder changes contents.
		""")

		main_menu.MENU_CHOICE = input("Choose an options: ")
		if main_menu.MENU_CHOICE=="1":
			log_alert()
		if main_menu.MENU_CHOICE=="2":
			credz()
		else:
			input("invalid option - PRESS ENTER")
			main_menu()

main_menu()
