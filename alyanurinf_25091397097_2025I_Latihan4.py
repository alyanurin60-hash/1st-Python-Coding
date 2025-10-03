bilangan1 = int(input("Masukkan bilangan (1-100): "))
bilangan2 = int(input("Masukkan bilangan (1-100): "))
bilangan3 = int(input("Masukkan bilangan (1-100): "))
if (bilangan1 >= bilangan2) and (bilangan1 >= bilangan3):
    terbesar = bilangan1
elif (bilangan2 >= bilangan1) and (bilangan2 >= bilangan3):
    terbesar = bilangan2
else:
    terbesar = bilangan3
print("Bilangan terbesar adalah:", terbesar)