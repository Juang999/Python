# name = str(input("input your name: "))

# print("hello ",name)

# print("boolean ", True)

# nilai1 = int(input("masukkan nilai pertama= "))
# nilai2 = int(input("masukkan nilai kedua= "))

# if nilai1 == 1 or nilai2 == 2: 
#   print("hello world")
# else:
#   print("tulisan salah!!!")

kelas = ["1A", "2A", "3A"]

print(kelas)

kelas_belakang = str(input("masukkan nama kelas untuk belakang: "))

kelas.append(kelas_belakang)

print(kelas)

kelas_depan = str(input("masukkan nama kelas depan: "))

kelas.insert(0, kelas_depan)

print(kelas)