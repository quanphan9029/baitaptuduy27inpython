print("Nhap ten va nam sinh cua 3 sinh vien de so sanh.")
sv1_name = input("Nhap ten sinh vien thu nhat: ")
namsinh1 = int(input("Nhap nam sinh cua sinh vien thu nhat: "))

sv2_name = input("Nhap ten sinh vien thu hai: ")
namsinh2 = int(input("Nhap nam sinh cua sinh vien thu hai: "))

sv3_name = input("Nhap ten sinh vien thu ba: ")
namsinh3 = int(input("Nhap nam sinh cua sinh vien thu ba: "))


def checkNamSinh():
	global namsinh1, namsinh2, namsinh3
	while namsinh1 < 0 or namsinh2 < 0 or namsinh3 < 0:
		if namsinh1 < 0:
			namsinh1 = int(input("Nam sinh cua sinh vien 1 khong duoc be hon 0. Moi nhap lai: "))
		elif namsinh2 < 0:
			namsinh2 = int(input("Nam sinh cua sinh vien 2 khong duoc be hon 0. Moi nhap lai: "))
		elif namsinh3 < 0:
			namsinh3 = int(input("Nam sinh cua sinh vien 3 khong duoc be hon 0. Moi nhap lai: "))


def checkAiLonHon():
	if namsinh1 > namsinh2 and namsinh1 > namsinh3:
		print("Sinh vien tre nhat la:", sv1_name)
	elif namsinh2 > namsinh1 and namsinh2 > namsinh3:
		print("Sinh vien tre nhat la:", sv2_name)
	elif namsinh3 > namsinh1 and namsinh3 > namsinh2:
		print("Sinh vien tre nhat la:", sv3_name)
	elif namsinh1 == namsinh2:
		if namsinh1 > namsinh3:
			print("Sinh vien tre nhat la: ",sv1_name," va ",sv2_name)
		else:
			print("Sinh vien tre nhat la: ",sv3_name)
	elif namsinh1 == namsinh3:
		if namsinh1 > namsinh2:
			print("Sinh vien tre nhat la: ",sv1_name, "va" , sv3_name)
		else:
			print("Sinh vien tre nhat la: ", sv2_name)
	elif namsinh2 == namsinh3:
		if namsinh2 > namsinh1:
			print("Sinh vien tre nhat la: ", sv2_name, "va", sv3_name)
		else:
			print("Sinh vien tre nhat la: ", sv1_name)
	else:
		print("3 sinh vien bang tuoi nhau.")


checkNamSinh()
checkAiLonHon()