def input_luas_dan_tinggi():
    alas = float(input("masukan alass :"))
    tinggi= float(input("masukan tinggi :"))
    print("luas =",0.5 * alas * tinggi)

    return alas, tinggi

def hitung_luas(alas , tinggi):
    return 0.5 * alas * tinggi

print(hitung_luas(5 , 10))
alas , tinggi = input_luas_dan_tinggi()
print(hitung_luas(alas , tinggi))