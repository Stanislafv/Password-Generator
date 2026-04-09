import random
while True:
    try:
        x = int(input("Сколько символов будет в пароле(От 4 до 16):"))
    except ValueError:
        print("Извините, но мы не поняли ваше число. Это точно число?")
        continue
    y = (["a", "b", "c","d", "g", "f","e", "i", "j","k", "l", "m","n", "o", "p","r", "s", "t","w", "v", "z","x", "y", "q","1", "2", "3","4", "5", "6","7", "8", "9","0", "!", "_",":", "?", ">","<", "~", "&","%", "@", ",",".", "#", "№"])


    if x == 4:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 5:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 6:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 7:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 8:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 9:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 10:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 11:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 12:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 13:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 14:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 15:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x == 16:
        print(random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y),random.choice(y), sep="")
    elif x >= 16:
        print("Число слишком велико, максимум: 16!")
    else:
        print("Число слишком маленькое, минимум 4!")