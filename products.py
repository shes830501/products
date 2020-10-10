import os #operating system


# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='UTF-8') as f:
		for line in f:
			if '商品名稱,商品價格' in line:
				continue #進行下一迴(跳過本迴)
			name, price = line.strip().split(',')
			products.append([name, price])	
	print(products)	

	return products

# 讓使用者輸入
def user_input(productss):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q': # quit
			break		
		price = int(input('請輸入商品價格: '))
		
		if price <= 0:
			print('商品價格不可為零或以下,請重新輸入')
		productss.append([name, price])
		#p = [name, price]
		#p = []
		#p.append(name)
		#p.append(price) 

	return productss

# 印出購買紀錄
def print_products(productsss):
	count = 0
	for p in productsss:
		print(p[0], '的價格是:', p[1])
		count = count + int(p[1]) # p[1]就是price  請看line 31
	print('總共是:', count)

	

# 寫入檔案
def write_file(filename, productsss):
	with open(filename, 'w', encoding='UTF-8') as f:
		f.write('商品名稱,商品價格\n')
		for p in productsss:
			f.write(p[0] + ',' + str(p[1]) + '\n')

# 執行檔案
def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 檢查檔案是否存在
		print('yeah! Here you are!')
		products = read_file(filename)
	else:
		print('Sorry!There is no file that you want.')
		
	productss = user_input(products) # 把上一行執行的結果投進
	print_products(productss) # 把上一行執行的結果投進
	write_file('products.csv', productss) # 把上一行執行的結果投進

main()