Jumlahbintang = int(input("masukan angka:"))
print()
  
for i in range(Jumlahbintang):
  print(' ' * (Jumlahbintang-i),end='')
  print('* ' * (i+1))
   
for i in range(1,Jumlahbintang):
  print(' ' * (i+1),end='')
  print('* ' * (Jumlahbintang-i))