print("Nhap vao 3 so nguyen de tim gia tri tuyet doi.")
so_1 = int(input("Nhap so nguyen thu nhat: "))
so_2 = int(input("Nhap so nguyen thu hai: "))
so_3 = int(input("Nhap so nguyen thu ba: "))

if (so_1 < 0):
	so_1*=-1
	print("Gia tri tuyet doi cua so thu nhat = " , so_1)
else:
	print("Gia tri tuyet doi cua so thu nhat = " , so_1)

if (so_2 < 0):
	so_2*=-1
	print("Gia tri tuyet doi cua so thu hai = " , so_2)
else:
	print("Gia tri tuyet doi cua so thu hai = " , so_2)

if (so_3 < 0):
	so_3*=-1
	print("Gia tri tuyet doi cua so thu ba = " , so_3)
else:
	print("Gia tri tuyet doi cua so thu ba = " , so_3)