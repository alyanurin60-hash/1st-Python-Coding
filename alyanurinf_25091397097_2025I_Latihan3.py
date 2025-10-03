usia= int(input("Masukkan usia (1-100):"))
tekanandarah= int(input("Masukkan tekanan darah (1-150):"))
if usia >=60 and  tekanandarah >140 :
    print(f"Status Kesehatan : Tinggi")
elif usia >=60 and tekanandarah <=140 :
    print(f"Status Kesehatan : Normal")
elif usia <60 and  tekanandarah >130 :
    print(f"Status Kesehatan : Tinggi")
elif usia <60 and tekanandarah <=130 :
    print(f"Status Kesehatan : Normal")
