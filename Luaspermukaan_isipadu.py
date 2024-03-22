#Atur cara mengira luaspermukaan dan isipadu silinder
#Isytihar pemalar 
pi=3.142

#input
jejari=float(input("Masukkan jejari:"))
tinggi=float(input("Masukkan tinggi:"))

#proses
Luas_permukaan=(2*pi*jejari*tinggi)+2*pi*(jejari**2)
Isi_padu=pi*(jejari**2)*tinggi

#output
print("Luas permukaan tangki air ialah",round(Luas_permukaan,2))
print("Isi padu tangki air ialah",round(Isi_padu,2))
