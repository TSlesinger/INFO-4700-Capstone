import subprocess
import os
import pyautogui
import time

def grab():
	print('Please import filepath for batch-process.')
	filepath = input()
	return filepath

def main():
	#Grab Filepath for Batch Processing
	filepath = grab()

	#Loop through all files in directory
	for root, dir, files, in os.walk(filepath):
		for file in files:
			#Find File Path of Song (need to not hard code)
			fp =  filepath +'\\' + str(file)
			print('Processing: ', fp)

			#Call Spek with that filepath
			subprocess.Popen(['C:\Program Files (x86)\Spek\Spek.exe', fp])

			time.sleep(2)			
			#Move Mouse to use Spek GUI
			pyautogui.FAIL_SAFE = True
			pyautogui.PAUSE = 1

			#pyautogui.moveTo(661, 1064) #Location of Spek on toolbar
			#pyautogui.click()
			pyautogui.hotkey('ctrl', 's')
			pyautogui.press('enter')
			pyautogui.hotkey('alt', 'f4')
			






if __name__ == '__main__':
  main()
