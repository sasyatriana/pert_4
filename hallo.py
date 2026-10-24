#24 oktober
#while
# hitung = 1                # 1. siapkan
# while hitung <= 3:        # 2. syarat berhenti
#     print(hitung)
#     hitung = hitung + 1   # 3. ubah nilainya

# #break
# for i in range(5):
#     if i == 2:
#         break
#     print(i)

#latihan
# nama = str(input("Masukkan nama: "))
# c = 1
# while c <= (len(nama)):
#     print(nama)
#     c = c + 1

# kuis1-FizzBuzz
# angka_Awal = int(input("masukkan angka: "))
# angka = int(input("masukkan batas angka: "))
# for i in range (angka_Awal, angka+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

#kuis2-nilai max
angka = []
while True:
    i = int(input("masukkan angka kedalam list. \n(ketik '-999' jika dirasa sudah cukup)\n:"))
    if i == -999:
        break
    angka.append(i)

print(f"Final list anda adalah {angka}")

if len(angka) == 0:
    print("List anda kosong. Tolong isi beberapa")
else:
    angka_terbesar = angka[0]
    for i in angka:
        if i > angka_terbesar:
            angka_terbesar = i
    print(f"Angka terbesar adalah {angka_terbesar}")
