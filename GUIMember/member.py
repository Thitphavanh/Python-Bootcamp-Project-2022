# member.py
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

conn = sqlite3.connect('member.sqlite3')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS memberinfo (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				memberid TEXT,
				first_name TEXT,
				last_name TEXT,
				tel TEXT,
				points INTEGER,
				note TEXT) """)

def InsertNewMember(memberid, first_name, last_name, tel, points, note):
	with conn:
		command = 'INSERT INTO memberinfo VALUES (?,?,?,?,?,?,?)'
		c.execute(command,(None, memberid, first_name, last_name, tel, points, note))
	conn.commit()
	print('Saved')

def ViewMember():
	with conn:
		command = 'SELECT * FROM memberinfo'
		c.execute(command)
		result = c.fetchall() # c.fetchone(), c.fetchmany(5)
	print(result)
	return result

def ViewOneMember(memberid):
	with conn:
		command = 'SELECT * FROM memberinfo WHERE memberid = (?)'
		c.execute(command, ([memberid]))
		result = c.fetchall() # c.fetchone(), c.fetchmany(5)
	print(result)
	return result

def DeleteMember(ID):
	with conn:
		command = 'DELETE FROM memberinfo WHERE ID = (?)'
		c.execute(command, ([ID]))
	conn.commit()
	print('{} : deleted'.format(ID))

def UpdateMember(ID, field, data):
	with conn:
		command = 'UPDATE memberinfo SET {} = (?) WHERE ID = (?)'.format(field)
		c.execute(command, ([data, ID]))
	conn.commit()
	print('{} : {} = {} updated'.format(ID, field, data))


#InsertNewMember('C1001','James','Sisavath',12345678,20,'newmember')
DeleteMember(19)
#UpdateMember(1, 'first_name', 'Noy')
ViewMember()
#ViewOneMember('C1002')

GUI = Tk()
GUI.geometry('900x600')
GUI.title('ໂປຣແກຣມບັນທຶກ member')


v_search = StringVar()
v_search.set('C1001')
search = ttk.Entry(GUI, textvariable = v_search, font = (None, 20), width = 15)
search.place(x = 50, y = 50)

def SearchMember():
	search = v_search.get()
	data = ViewOneMember(search)
	if len(data) >= 1:
		data = data[0]
		v_memberid.set(data[1])
		v_first_name.set(data[2])
		v_last_name.set(data[3])
		v_tel.set(data[4])
		v_points.set(data[5])
		v_note.set(data[6])
	else:
		messagebox.showwarning('Not found','ບໍ່ມີສະມາຊິກຄົນນີ້ ກະລຸນາກວດສອບລະຫັດສະມາຊິກໃຫ້ຖືກຕ້ອງ')

frameButton1 = Frame(GUI)
frameButton1.place(x = 90, y = 100)
searchButton = ttk.Button(frameButton1, text = 'ຄົ້ນຫາຊື່ສະມາຊິກ', command = SearchMember)
searchButton.pack(ipadx = 30, ipady = 20)

#-------------Right--------------
frameButton2 = Frame(GUI)
frameButton2.place(x = 350, y = 100)

v_memberid = StringVar()
L = Label(frameButton2, text = 'ລະຫັດສະມາຊິກ', font = (None, 10)).pack()
E1 = ttk.Entry(frameButton2, textvariable = v_memberid, font = (None, 20), width = 30)
E1.pack()

v_first_name = StringVar()
L = Label(frameButton2, text = 'ຊື່', font = (None, 10)).pack()
E2 = ttk.Entry(frameButton2, textvariable = v_first_name, font = (None, 20), width = 30)
E2.pack()

v_last_name = StringVar()
L = Label(frameButton2, text = 'ນາມສະກຸນ', font = (None, 10)).pack()
E3 = ttk.Entry(frameButton2, textvariable = v_last_name, font = (None, 20), width = 30)
E3.pack()

v_tel = StringVar()
L = Label(frameButton2, text = 'ເບີໂທລະສັບ', font = (None, 10)).pack()
E4 = ttk.Entry(frameButton2, textvariable = v_tel, font = (None, 20), width = 30)
E4.pack()

v_points = StringVar()
L = Label(frameButton2, text = 'ຄະແນນ', font = (None, 10)).pack()
E5 = ttk.Entry(frameButton2, textvariable = v_points, font = (None, 20), width = 30)
E5.pack()

v_note = StringVar()
L = Label(frameButton2, text = 'ອື່ນໆ', font = (None, 10)).pack()
E6 = ttk.Entry(frameButton2, textvariable = v_note, font = (None, 20), width = 30)
E6.pack()

frameButton2 = Frame(GUI)
frameButton2.place(x = 500, y = 520)
saveButton = ttk.Button(frameButton2, text = 'ບັນທຶກ/ອັພເດຕ')
saveButton.pack(ipadx = 30, ipady = 20)

GUI.mainloop()