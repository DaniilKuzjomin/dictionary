
rus=[]
ang=[]


def main():
    global rus
    global ang
    print("Добро пожаловать в Русско-Английский словарь!")
    print("Выберите с какого на какой язык Вы хотите перевести слово(-а)")
    print()
    print("1 - Перевести Ваше слово")
    print("2 - показать список существующих слов")
    print("3 - добавить Ваше слово(-а) в существующий список")
    vibor=int(input("-> "))
    if vibor==1:
        translate(ang,rus)
    if vibor==2:
        print("Выберите какой список слов Вы хотите посмотреть.")
        print()
        print("1 - Русский список слов")
        print("2 - Английский список слов")
        vibor_s=int(input("-> "))
        if vibor_s==1:
            rus=failist_lugemine("rus.txt",rus)
            print(rus)
        if vibor_s==2:
            ang=failist_lugemine("ang.txt",ang)
            print(ang)
        else:
            print("Error.")


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

def translate(l1:list,l2:list):
    slovo=input("Введите слово которое Вы хотите перевести -> ")
    if slovo in l1:
        trans=l2[l1.index(slovo)]
        print(slovo+"-"+ trans)
    elif slovo in l2:
        trans=l1[l2.index(slovo)]
        print(slovo+"-"+trans)
    else:
        print("К сожалению данное слово отсутcвует в списке.")
        print()
    print("Хотите ли Вы добавить вписанное слово в список?")

def correction(word:str,l:list):
    for i in range(len(l)):
        if l[i]==word:
            new_word==word.replace(word,input("Новое слово -> "))
            l.insert(i,new_word)
            l.remove(word)
    return l


# rus=novoe_slovo("rus.txt",input("Введите новое слово ->"))
