# GUI.py
from tkinter import *
from tkinter import ttk, messagebox

friend = {'James':'Sisavath','Jo':'Sipasuet','Noy':'Sivilay'}

GUI = Tk()
GUI.title('My Program')
GUI.geometry('400x300')

L = Label(GUI,text='ກະລຸນາໃສ່ລະຫັດຊື່').pack(pady=10)

v_text = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_text)
E1.pack(ipadx=10,ipady=10,pady=10)

def Click():
	text = v_text.get()
	print('Text: ',text)
	if text in friend:
		result = friend[text]
		messagebox.showinfo('Result','ຊື່ : {} ນາມສະກຸນ : {}'.format(text,result))
	else:
		print('ບໍ່ມີຂໍ້ມູນຂອງຄົນນີ້')
		messagebox.showwarning('Result: Error','ບໍ່ມີຂໍ້ມູນໃນລະບົບ ກະລຸນາໃສ່ຂໍ້ມູນ ຫຼືເພີ່ມເຂົ້າໃນລະບົບ')


B1 = ttk.Button(GUI, text='Click me!',command=Click)
B1.pack(ipadx=30,ipady=10,pady=10)

GUI.mainloop()

