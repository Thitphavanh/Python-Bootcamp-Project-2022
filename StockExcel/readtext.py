def readtext(filename = 'stocklist.txt'):
	with open(filename, encoding = 'utf-8') as file:
		lines = file.read()

	result = lines.split('\n')
	stockname = []
	for r in result:
		if r != '':
			stockname.append(r)
	return stockname

	