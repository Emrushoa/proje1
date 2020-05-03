print ("Bu Program Girilen 5 Sayıyı Küçükten Büyüğe Sıralar")
print ("Programlayıcı: Emre Erdem")
print ("")

s1=float(input('Lütfen 1.Sayıyı Giriniz: '))
s2=float(input('Lütfen 2.Sayıyı Giriniz: '))
s3=float(input('Lütfen 3.Sayıyı Giriniz: '))
s4=float(input('Lütfen 4.Sayıyı Giriniz: '))
s5=float(input('Lütfen 5.Sayıyı Giriniz: '))
ilk_sira=[s1,s2,s3,s4,s5]
artan_sira=sorted(ilk_sira)
azalan_sira=sorted(ilk_sira, reverse=True)

print("Girdiğiniz Sayılar: ",ilk_sira)
print("Küçükten Büyüğe Sıralı Liste:", artan_sira)
print("Büyükten Küçüğe Sıralama", azalan_sira)


