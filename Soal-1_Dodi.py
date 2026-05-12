# Tampilannya bersih pas di RUN
import os 
os.system('cls')

# Menurut saya program ini di gunakan untuk menghitung Jumlah semua digit dalam sebuah bilangan secara rekursif

def jumlah_digit(n) :
# Jila bilangan hanya satu digit,langsung kembalikan nilainya
    if n <10 :
        return n
# Ambil digit terakhir (n % 10),lalu jumlahkan dengan hasil rekursif dari sisa bilangan (n // 10)
    return (n % 10) + jumlah_digit(n//10)
# Input angka yang mau anda masukan
angka = int(input("Masukan bilangan : "))
# Proses perhitungan
hasil = jumlah_digit(angka)
# Menampilkan hasil dari proses
print("jumlah_digit dari =",angka,"adalah",hasil)