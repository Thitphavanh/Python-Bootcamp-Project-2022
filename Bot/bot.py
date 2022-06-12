# bot.py
import webbrowser
import time
import pyautogui
import pyperclip
import os

thaichr = [ chr(i) for i in range(3585, 3676)]
def isThai(word):
	for w in word:
		if w in thaichr:
			print('Thai')
			return True
	print('Other Language')
	return False
	
def Search(keyword = 'Thailand'):
	url = 'https://www.google.com'
	webbrowser.open(url)
	time.sleep(2)

	if isThai(keyword):
		pyperclip.copy(keyword)
		time.sleep(0.5)
		pyautogui.hotkey('ctrl','v')
	else:
		pyautogui.write(keyword,interval=0.25)

	pyautogui.press('enter')
	time.sleep(1)
	path = r'C:\Users\Hery\Desktop\Python Bootcamp 2022\Capture\Search'
	filename = os.path.join(path, '{}.jpg'.format(keyword))
	pyautogui.screenshot(filename)
	time.sleep(1)
	pyautogui.hotkey('ctrl','w')

wordlist = ['ลาว','usa','uk','อิตาลี']
for s in wordlist:
	Search(s)