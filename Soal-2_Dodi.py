# Tampilannya bersih pas di RUN
import os 
os.system('cls')

# Menurut saya program ini di gunakan untuk menghitung pangkat bilangan secara rekursif

def pangkat (a,b) :
# Jika pngkat bilangan 0,hasilnya 1
    if b == 0 :
        return 1
# Bilangan di kalikan dengan dirinya sendiri sebanyak nilai pangkat
    return a * pangkat (a,b-1)
# Input bilangan pokok
a = int(input("Masukan bilangan pokok : "))
# Input nilai pangkat
b = int(input("Masukan nilai pangkat : "))
# Proses menghitung
hasil = pangkat(a,b)
# Tampilkan hasil dari proses
print(a,"^",b, "=",hasil)