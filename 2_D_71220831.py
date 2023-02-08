a = "vito dan farel sedang bermain bola bersama jono, si tono juga bergabung bermain bola juga, kemudian datanglah inug dan mereka tidak jadi bermain bola"
kata=input("kalimat yang ingin diteliti:").lower().split()
b=input("kata yang ingin dicari:")
jumlah=0
for i in kata:
    if i==b:
        jumlah+=1
print(jumlah)