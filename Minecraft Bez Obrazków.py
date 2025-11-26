import random
import time
def fight(Wojownik, Boss):
    while Wojownik['hp']>0 or Boss['hp']>0:
        Boss['hp']-=Wojownik['power']
        print(Wojownik['name'] + ' zadał ' + Boss['name'] + ' ' + str(Wojownik['power'])
              + ' hp. ' + 'Bossowi zostało ' + str(Boss['hp']))
        time.sleep(0.67)
        if Boss['hp']<=0:
            print(Wojownik['name'] + ' pokonał ' + Boss['name'])
            zdobytehajsiwo = random.randint(31, 62)
            Wojownik['gold']+=zdobytehajsiwo
            break
        else:
            Wojownik['hp']-=Boss['power']
            print(Boss['name'] + ' zadał ' + Wojownik['name'] + ' ' + str(Boss['power'])
                  +  ' hp. ' + 'Zostało ci ' + str(Wojownik['hp']))
            time.sleep(0.67)
            if Wojownik['hp']<=0:
                print(Boss['name'] + ' niestety cię unicestwił')
                break
Wojownik = {
    'name': 'SharkyDominik',
    'power': 5,
    'hp': 10,
    'gold': 0
}
Ender_Dragon = {
    'name': 'Ender_Dragon',
    'power': 10,
    'hp': 500
}
Wither = {
    'name': 'Wither',
    'power': 20,
    'hp': 300
}
Warden = {
    'name': 'Warden',
    'power': 30,
    'hp': 250
}
Player = Wojownik.copy()
while True:
    print('Gdzie Idziesz? \n 1.Tawerna \n 2.OverWorld \n 3.Nether \n 4.End \n 5.Bank \n 6.DrugiŚwiat \n 7.Quit')
    GdzieIdziesz = input()
    if GdzieIdziesz == '1'or GdzieIdziesz == ' 1':
        print('Wchodzisz do Buda Dla Grubasów')
        print('Co chcesz zrobić? \n 1.Odzyskać hp \n 2.Handluj \n 3.Idź gdzie indziej')
        WybórTawerna = input()
        if WybórTawerna == '3':
            continue
        elif WybórTawerna == '1':
            Player['hp'] = Wojownik['hp']
            print('odrodzono hp')
            continue
        elif WybórTawerna == '2':
            print('buy or sell? \n 1.buy \n 2.sell')
            BuyOrSell = input()
            if BuyOrSell == '1':
                continue
            elif BuyOrSell == '2':
                continue
            else:
                print('Nerosume nerosume to sie uczy to rosume')
                continue
        else:
            print('Nerosume nerosume to sie uczy to rosume')
            continue
    elif GdzieIdziesz == '4' or GdzieIdziesz == ' 4':
        fight(Player, Ender_Dragon)
    elif GdzieIdziesz == '7' or GdzieIdziesz == ' 7':
        print('Nara nikt cie nie potrzebuje')
        break
    else:
        print('Nerosume nerosume to sie uczy to rosume')
