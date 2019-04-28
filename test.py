import subprocess
import os
import time

def main():
	p = subprocess.Popen([r'C:\Users\spitf_000\Downloads\spek-0.8.2\Spek\spek.exe', r'C:\DJ Music\HDD Recovery\03 Juices.mp3'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

	poll = p.poll()

	time.sleep(10)

	if poll == None:
		print('good')

	else:
		print('bad')

if __name__ == '__main__':
	main()