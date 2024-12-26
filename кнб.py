print("""ДОбро пожаловать в игру КАМЕНЬ НОЖНИЦЫ БУМАГА
Своим появлением на свет в 1931 году эта игра обязана Великой экономической депрессии в США.
В поисках заработка американский инженер Милтон Брэдли после ряда безуспешных попыток основать
собственный бизнес на продаже литографий Авраама Линкольна решил продавать настольные игры.
 Причем в те годы в США они не имели абсолютно никакой популярности.""")

print("С НОВЫМ ГОДОМ:🎁🎄")


firstplayer = input("Ход первого игрока: ")
secondplayer = input("Ход второго игрока: ")
bonusfirst = 0 
bonussecond = 0
while True:
    if firstplayer.lower() == "ножницы" and secondplayer.lower() == "камень":
        
        bonussecond += 1
        print("Второй игрок. Счёт :",bonussecond  )
         
    elif firstplayer.lower() == "ножницы" and secondplayer.lower() == "бумага":

        bonusfirst += 1
        print("первый игрок. Счёт :",firstplayer  )

    elif firstplayer.lower() == "ножницы" and secondplayer.lower() == "ножницы":
    
        bonusfirst += 1
        bonussecond += 1 
        print("ничья. Счет :",firstplayer, secondplayer ) 

    elif firstplayer.lower() == "камень" and secondplayer.lower() == "камень":

        bonusfirst += 1
        bonussecond += 1
        print("ничья. Счет :",firstplayer, secondplayer )

    elif firstplayer.lower() == "камень" and secondplayer.lower() == "бумага":

        bonussecond += 1
        print("второй игрок. Счет :",bonussecond ) 

    elif firstplayer.lower() == "камень" and secondplayer.lower() == "ножницы":

        bonusfirst += 1
        print("первый игрок. Счет :",bonusfirst )

    elif firstplayer.lower() == "бумага" and secondplayer.lower() == "бумага":

        bonussecond += 1
        bonusfirst += 1
        print("ничья. Счет :",bonusfirst, bonussecond )

    elif firstplayer.lower() =="бумага" and secondplayer.lower() == "ножницы":

        bonussecond += 1
        print("воторй игрок. Счет :",bonussecond )

    elif firstplayer.lower() == "бумага" and secondplayer.lower() == "камень":

        bonusfirst += 1
        print("первый игрок. Счет :",bonusfirst)

    firstplayer = input("Ход первого игрока: ")
    secondplayer = input("Ход второго игрока: ")

