# GUIStock.py
from tkinter import *
from tkinter import ttk, filedialog
from urllib.request import urlopen as req # as req คือ การตั้งคำสั้นๆ
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
from datetime import datetime
import subprocess

#---------Stock Library-------------
def StockPrice(CODE='PTT'):

	url = f'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={CODE}&ssoPageId=10&selectPage=2'

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()

	data = soup(page_html,'html.parser')
	result = data.find_all('div',{'class':'col-xs-6'})

	title = result[0].text
	price = float(result[2].text)
	change = result[3].text.replace('\n','')
	change = change.replace('\r','').replace(' ','').replace('\t','')
	change = float(change[11:]) # ຕັດຄຳວ່າ ປ່ຽນແປງ ອອກໄປ
	pchange = result[4].text.replace('\n','').replace('\r','').replace(' ','').replace('\t','')
	pchange = float(pchange[12:-1]) # ຕັດຄຳວ່າ %ປ່ຽນແປງ ແລະ % ດ້ານຫຼັງອອກໄປ
	print('Stock: {} Price: {} Change: {} %Change: {}'.format(title,price,change,pchange))
	return (title,price,change,pchange)


#--------------ກຽມຂໍ້ມູນ#--------------
def readtext(filename='stocklist.txt'):
	with open(filename,encoding='utf-8') as file:
			lines = file.read()

	result = lines.split('\n')
	stockname = []
	for r in result:
		if r != '':
			stockname.append(r)
	return stockname


GUI = Tk()
GUI.geometry('600x400')
GUI.title('ໂປຣແກຣມກວດສອບລາຄາຫຸ້ນຈາກໄຟລ໌ txt')

L = Label(GUI,text='ກະລຸນາເລືອກໄຟລ໌ (.txt) ທີ່ມີລາຍຊື່ຫຸ້ນຢູ່ພາຍໃນ',font=(None,15)).pack()

v_path = StringVar()

def SelectFile():
	path = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("TXT files", "*.txt"),("all files", "*.*")))
	print(path)
	v_path.set(path)

B1 = ttk.Button(GUI,text='ເລືອກໄຟລ໌ (.txt)',command=SelectFile)
B1.pack(ipadx=20,ipady=10,pady=10)

def ExporttoExcel():
	# stocklist = ['SRICHA','TTCL','TOPP','TWZ','CIVIL','SIRIP','PRECHA','SNC','DEMCO','SPRC']
	stocklist = readtext(v_path.get())

	result = [] # [[1,'PTT',50,+3,1.56%],[1,'SCB',150,+5,2%]]

	for i,st in enumerate(stocklist,start=1):
		tt,pc,ch,pch = StockPrice(st)
		result.append( [i,tt,pc,ch,pch] )
		#print(i,tt,pc,ch,pch)

	excelfile = Workbook()
	sheet = excelfile.active
	sheet.title =  datetime.now().strftime('%Y-%m-%d %H|%M|%S') #'2022-FEB-06'

	header = ['No.','Stock','Price','Change (Baht)','%Change (%)']
	sheet.append(header)
	# sheet.append(StockPrice('SRICHA'))

	for rs in result:
		sheet.append(rs)

	excelfile.save('StockExcel.xlsx')
	subprocess.Popen('StockExcel.xlsx',shell=True)


B2 = ttk.Button(GUI,text='ກວດສອບລາຄາລ່າສຸດ export ເປັນ excel',command=ExporttoExcel)
B2.pack(ipadx=20,ipady=10,pady=10)

R = Label(GUI,textvariable=v_path).pack()

GUI.mainloop()