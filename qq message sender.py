# This code is by mzWyt. 20-03-25
##############################################################

import time
import win32gui
import win32con
import win32clipboard as w
import random


target_time = [649, 750]
last_time = 0


def send_message(name, msg):
	w.OpenClipboard()
	w.EmptyClipboard()
	w.SetClipboardData(win32con.CF_UNICODETEXT, msg)
	w.CloseClipboard()

	try:
		handle = win32gui.FindWindow(None, name)
	except:
		print("WindowError")
	win32gui.SendMessage(handle, 770, 0, 0)

	win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)

def timer(gap):
	while True:
		req_time = time.localtime(time.time())
		curr_time = req_time.tm_hour * 100 + req_time.tm_min 
		print("Time checked. Current time: " + str(curr_time))
		if curr_time in target_time and curr_time != last_time:
			print("Time checked and it's set time now.")
			send_message("我的iPhone", "test")
			last_time = curr_time
		time.sleep(gap)

def MAIN():
	timer(60)



