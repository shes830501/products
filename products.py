products = []
count = 0
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': # quit
		break
	
	price = int(input('請輸入商品價格: '))
	if price <= 0:
		print('商品價格不可為零或以下,請重新輸入')
	count = count + price
	products.append([name, price])
	#p = [name, price]
	#p = []
	#p.append(name)
	#p.append(price) 
for p in products:
	print(p[0], '的價格是:', p[1])
print('總共是:', count)

with open('products.csv', 'w', encoding='UTF-8') as f:
	f.write('商品名稱,商品價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')