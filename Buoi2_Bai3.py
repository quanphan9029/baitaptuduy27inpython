print("Nhap vao 5 so nguyen.")
so_1 = int(input("Nhap vao so nguyen thu nhat: "))
so_2 = int(input("Nhap vao so nguyen thu hai: "))
so_3 = int(input("Nhap vao so nguyen thu ba: "))
so_4 = int(input("Nhap vao so nguyen thu tu: "))
so_5 = int(input("Nhap vao so nguyen thu nam: "))

demChan = 0
demLe = 0

if so_1 % 2 == 0:
	demChan = demChan + 1
else:
	demLe += 1
if so_2 % 2 == 0:
	demChan = demChan + 1
else:
	demLe += 1
if so_3 % 2 == 0:
	demChan = demChan + 1
else:
	demLe += 1
if so_4 % 2 == 0:
	demChan = demChan + 1
else:
	demLe += 1
if so_5 % 2 == 0:
	demChan = demChan + 1
else:
	demLe += 1

print("Co ",demChan," so chan.")
print("Co ",demLe," so le.")