# stock
from urllib.request import urlopen as req # as req ແມ່ນ ການຂຽນຊື່ຫຍໍ້
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
from datetime import datetime

#-----------Stock Library-----------
def StockPrice(CODE='PTT'):

	url = f'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={CODE}&ssoPageId=10&selectPage=2'

	webopen = req(url)
	page_html = webopen.read()
	webopen.close()
	data = soup(page_html, 'html.parser')
	result = data.find_all('div', {'class':'col-xs-6'})

	title = result[0].text
	price = float(result[2].text)
	change = result[3].text.replace('\n','').replace('\r','').replace(' ','').replace('\t','')
	change = float(change[11:]) # ຕັດຄຳວ່າ ປ່ຽນແປງ ອອກໄປ
	perchange = result[4].text.replace('\n','').replace('\r','').replace(' ','').replace('\t','')
	perchange = float(perchange[12:-1]) # ຕັດຄຳວ່າ %ປ່ຽນແປງ ແລະ % ດ້ານຫຼັງອອກໄປ

	print('Stock : {}, Price : {}, Change : {}, %Change : {}'.format(title, price, change, perchange))
	return (title,price,change,perchange)

#--------------ກຽມຂໍ້ມູນ#--------------
def readtext(filename = 'stocklist.txt'):
	with open(filename, encoding = 'utf-8') as file:
		lines = file.read()

	result = lines.split('\n')
	stockname = []
	for r in result:
		if r != '':
			stockname.append(r)
	return stockname
#stocklist = ['SRICHA','TTCL','TOPP','TWZ','CIVIL','SIRIP','PRECHA','SNC','DEMCO','SPRC']
stocklist = readtext('bank.txt')
result = [] # [[1, 'PTT', 50, +3,3.5%], [2, 'KBANK', 150, +6,3.5%]]

for i, st in enumerate(stocklist, start = 1):
	tt, pc, ch, pch = StockPrice(st)
	result.append([i, tt, pc, ch, pch])
    # print(i, tt, pc, ch, pch)
# print(result)

#-------Export data to Excel#--------

excelfile = Workbook()
sheet = excelfile.active
sheet.title = datetime.now().strftime('%Y-%m-%d %H|%M|%S') #'2022-Feb-06'

header = ['No.','Stock','Price','Change (Bath)','%Change (%)']
sheet.append(header)
# sheet.append(StockPrice('SRICHA'))

for rs in result:
	sheet.append(rs)

excelfile.save('StockExcel.xlsx')
