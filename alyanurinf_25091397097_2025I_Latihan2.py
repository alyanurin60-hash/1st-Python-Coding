nilai= int(input("Masukkan nilai (1-100):"))
if nilai >=90 and  100 :
    print(f"Status : Sangat Baik")
elif nilai >=80 and 89:
    print(f"Status : Baik")
elif nilai >=70 and 79:
    print(f"Status : Cukup")
elif nilai >=60 and 69:
    print(f"Status : Kurang")
else: 
    print(f"Status : Sangat Kurang")