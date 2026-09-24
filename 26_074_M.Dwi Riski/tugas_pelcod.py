
nama = input ("masukkan nama:")
umur = int(input ("masukkan umur:"))
tinggi = (input ("masukkan tinggi badan:"))
angka_favorit = int (input("masukkan angka favoritmu:"))


print("\n=====OUTPUT1=====")
print("Hai Perkenalkan Nama Saya :", nama)
print("Saya Berumur :",umur)
print("tinggi saya :", tinggi)
print("angka_favoritku adalah :", angka_favorit)

pensil = 4 * 2000 
buku = 2 * 5000  
total = pensil + buku

print("\n=====OUTPUT2=====")
print ("total", total)

print("\n=====OUTPUT3=====")
if angka_favorit % 2==0 :
    print ("angka Genap")
else :
    print ("angka Ganjil")