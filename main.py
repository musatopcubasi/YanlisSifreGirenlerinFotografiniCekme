import cv2  #fotoğraf çekmek için

import imghdr
import smtplib  #3ü de mail ile göndermek için
from email.message import EmailMessage

class Guvenlik:
    def __init__(self,sifre):
        self.sifre=sifre
        self.girisDurumu=False

    def menu(self):
        print("""
        1-Şifre Değiştir
        2-Giriş Yap
        3-Çıkış
            """)
        print(self.sifre)
        self.secim()

    def secim(self):
        secim=int(input("Seçiminizi giriniz"))
        if secim==1:
            self.sifreDegistir()
        elif secim==2:
            self.sifredogruMu(self.sifregir())
        elif secim==3:
            self.cikisyap()


    def sifreDegistir(self):
        sifregirilen=self.sifregir()
        sifre=self.sifre
        if sifre==sifregirilen:
            print("Yeni şifre")
            yenisifre=self.sifregir()
            self.sifre=yenisifre
            print(yenisifre)
            self.menu()
        else:
            print("Şifreniz yanlış")
            self.menu()

    def cikisyap(self):
        self.girisDurumu=False
        print("Çıkış yapılıyor")

    def sifregir(self):
        girilenSifre=int(input("Sifre Gir"))
        return girilenSifre

    def girisYap(self):
        self.girisDurumu=True
        print("Giriş Yapıldı")
        self.menu()


    def sifredogruMu(self,sifregirilen):

        if self.sifre == sifregirilen:
            self.girisYap()
        else:
            self.sifreYanlis()

    def sifreYanlis(self):
        print("Girdiğiniz şifre yanlış tekrar deneyin")
        self.sifregir()
        self.resimCek()

    def resimCek(self):
        kamera=cv2.VideoCapture(0,cv2.CAP_DSHOW)#hata almamızı engellemek için cv2.CAP_DSHOW parametresini ekledik
        ret,kare=kamera.read()
        cv2.imwrite('sahis.png', kare)
        self.resmiMailIleGonder()
        kamera.release()
        cv2.destroyAllWindows()

    def resmiMailIleGonder(self):

        mesaj = EmailMessage()

        mesaj["Subject"] = "Resim gönderme"
        mesaj["From"] = "DOLDURUN"# kullanılacak hesap
        mesaj["To"] = "DOLDURUN" # gönderilecek hesap

        mesaj.set_content("Eklenti Denemesi")

        with open("sahis.png", "rb") as f:
            img_data = f.read()
            img_name = f.name
            img_type = imghdr.what(f.name)

        mesaj.add_attachment(img_data, maintype="image", subtype=img_type, filename=img_name)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login("DOLDURUN", "DOLDURUN")# giriş yapıyoruz
            smtp.send_message(mesaj)

guvenlik=Guvenlik(1234)
guvenlik.menu()
