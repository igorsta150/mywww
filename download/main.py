from time import sleep
import random, string

wybor = -1
wybor2 = -1
kasa = 10

nick = input("Podaj swoją nazwę użytkownika: ")
print(f"Witaj {nick} w grze Lotto!")
print("Gra polega na losowaniu nagród")
print("Na początek dostajesz 10$")
print("Uwaga!!!")
print("Po wyjściu z gry, gra się resetuje")

while wybor !=3:
    if wybor ==1:
        print(f"Aktualnie posiadasz: {kasa}$")
    if wybor ==2:
        wybor2 = -1
        while wybor2 !=4:
            if wybor2 ==1:
                kasa = kasa - 3
                kuponnormalny =('').join(random.choices(string.digits, k=1))
                kasa = kasa + int(kuponnormalny)
                print(f"Wygrałeś {kuponnormalny}$! Aktualnie posiadasz {kasa}$")
            if wybor2 ==2:
                kasa = kasa - 10
                kuponspecjalny =('').join(random.choices(string.digits, k=1))
                kuponspecjalny2 =('').join(random.choices(string.digits, k=1))
                kuponspecjalny = int(kuponspecjalny) + int(kuponspecjalny2)
                kasa = kasa + int(kuponspecjalny)
                print(f"Wygrałeś {kuponspecjalny}$! Aktualnie posiadasz {kasa}$")
            if wybor2 ==3:
                kasa = kasa - 25
                kuponpremium =('').join(random.choices(string.digits, k=2))
                kasa = kasa + int(kuponpremium)
                print(f"Wygrałeś {kuponpremium}$! Aktualnie posiadasz {kasa}$")
            print("")
            print("Wybierz który kupon chcesz kupić:")
            print("")
            print("1. Kupon Normalny - 3$")
            print("2. Kupon Specjalny - 10$")
            print("3. Kupon Premium - 25$")
            print("4. Anuluj")
            print("")
            wybor2 = int(input("Wybierz Opcje: "))
    print("")
    print("Menu:")
    print("1. Stan konta")
    print("2. Zakup kuponu")
    print("4. Wyjście z gry")
    print("")
    wybor = int(input("Wybierz Opcje: "))
    print("")