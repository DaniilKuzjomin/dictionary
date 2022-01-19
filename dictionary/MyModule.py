
rus=[]
ang=[]


def main():
    print("Добро пожаловать в Русско-Английский словарь!")
    print("Выберите с какого на какой язык Вы хотите перевести слово(-а)")
    print()
    print("1 - с Русского на Английский")
    print("2 - с Английского на Русский")
    print("3 - показать список существующих слов")
    print("4 - добавить Ваше слово(-а) в существующий список")
    vibor=int(input("-> "))
    if vibor==1:
        print("Введите слово ( на Русском ) которое Вы хотите перевести.")
        slovo_rus=str(input("-> "))
    if vibor==2:
        print("Введите слово ( на Английском ) которое Вы хотите перевести.")
        slovo_eng=str(input("-> "))
    if vibor==3:
        print("Выберите какой список слов Вы хотите посмотреть.")
        print()
        print("1 - Русский список слов")
        print("2 - Английский список слов")
        vibor_s=int(input("-> "))
        if vibor_s==1:
            global rus
            rus=failist_lugemine("rus.txt",rus)
            print(rus)
        if vibor_s==2:
            global ang
            ang=failist_lugemine("ang.txt",ang)
            print(ang)
        else:
            print("Error.")
    if vibor==4:












def failist_lugemine(f:str,l:list):
    """Info failist f listsisse l
    """
    fail=open(f,"r",encoding="utf-8-sig") #,encoding="utf-8-sig"
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l

def failisse_salvestamine(f:str,l:list):
    """Loetelu salvestame failisse
    """
    fail=open(f,"w")
    for el in l:
        fail.write(el+"\n")
    fail.close()

def rida_salvestamine(f:str,rida:str):
    """Üks sõna või lause(rida) salvestame failisse
    """
    fail=open(f,"a")
    fail.write(rida+"\n")
    fail.close()




# rus=novoe_slovo("rus.txt",input("Введите новое слово ->"))