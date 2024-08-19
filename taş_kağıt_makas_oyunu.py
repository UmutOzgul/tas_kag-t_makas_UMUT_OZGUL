import random

def tas_kagit_makas_UMUT_OZGUL():
    print("Taş, kağıt, makas oyununa hoş geldin!")
    print("Bu oyun 3 turdan oluşur ve 2 turu kazanan galip gelir. Tabii ki beni yenebilirsen!")
    print("Kuralları bilmiyorsan hatırlatayım: Taş, makası yener. Kağıt, taşı yener. Makas, kağıdı yener sonrası Hande Yener SAKAAA TAAMAM.")
    print("O zaman başlayalım. Bakalım beni yenebilecek misin?")

    seçimler = ("taş", "kağıt", "makas", "çıkış")

    oyuncu_win = 0
    bilgisayar_win = 0

    while oyuncu_win < 2 and bilgisayar_win < 2:
        bilgisayar_seçim = random.choice(seçimler[:-1])
        oyuncu_seçim = input(f"Seçimini yap bakalım {seçimler}: ").lower()

        if oyuncu_seçim == "çıkış":
            print("O zaman neden geldin? Ben robotum diye zamanım önemsiz öyle mi? Neyse, görüşürüz!")
            return
        elif oyuncu_seçim not in seçimler[:-1]:
            print("Geçersiz giriş yaptın. Kuralları ne çabuk unuttun!")
            continue
        else:
            print(f"Benim seçimim: {bilgisayar_seçim}")
            print(f"Senin seçimin: {oyuncu_seçim}")

        if oyuncu_seçim == bilgisayar_seçim:
            print("Berabere kaldık!")
        elif (oyuncu_seçim == "taş" and bilgisayar_seçim == "makas") or \
             (oyuncu_seçim == "kağıt" and bilgisayar_seçim == "taş") or \
             (oyuncu_seçim == "makas" and bilgisayar_seçim == "kağıt"):
            oyuncu_win += 1
            print("Bu turu kazandın. Tebrikler!")
        else:
            bilgisayar_win += 1
            print("Bu turu ben kazandım. Hah!")

        print(f"Tur Skoru: Oyuncu {oyuncu_win} - {bilgisayar_win} Bilgisayar")

    if oyuncu_win == 2:
        print("TAMAM SEN KAZANDINNN. Tebrikler!")
    elif bilgisayar_win == 2:
        print("HAHA! Ben kazandım!")

    devamlılık = ["evet","hayır"]
    oyun_devamı = input(f"Oyuna devam etmek ister misin? {devamlılık} : ").lower()
    if oyun_devamı == "evet":
        tas_kagit_makas_UMUT_OZGUL()
    else:
        print("Oyun bitti. Görüşürüz!")

if __name__ == "__main__":
    tas_kagit_makas_UMUT_OZGUL()
