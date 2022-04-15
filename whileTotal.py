print("""********************************
Girilen Sayıların Toplamı Programı
********************************""")

toplam = 0

while True:
  sayi = input("Bir Sayı Giriniz(Çıkmak için 'q' tuşuna basınız): ")
  
  if (sayi == "q"):
    print("Programdan Çıkıldı.")
    break
  else:
    toplam += int(sayi)
    print("Girilen Sayıların Toplamı: ",toplam)