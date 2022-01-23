

rus=[]
ang=[]


def main():
    global rus
    global ang
    print("Добро пожаловать в Русско-Английский словарь!")
    print("Выберите с какого на какой язык Вы хотите перевести слово(-а)")
    print()
    print("1 - Перевести Ваше слово")
    print("2 - Показать список существующих слов")
    print("3 - Добавить Ваше слово(-а) в существующий список")
    print("4 - Исправить ошибку в слове")
    print("5 - Проговорить выбранное Вами слово")
    print("6 - Проверка знаний по словам из списка")
    vibor=int(input("-> "))
    if vibor not in [1,2,3,4,5,6]:
      print("Ошибка, введите число от 1 до 6.")
    else:
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
      if vibor==3:
        new_word()
      if vibor==4:
        correction(rus,"rus.txt",ang,"ang.txt")
      if vibor==5:
        print("Введите слово которое Вы хотите проговорить.")
        word=input("-> ")
        print("На каком языке Вы хотите проговорить слово?")
        language=input("-> ")
        heli(word,language)
      if vibor==6:




def failist_lugemine(f:str,l:list):
    """Info failist f listsisse l
    """
    fail=open(f,"r",encoding="utf-8-sig") #,encoding="utf-8-sig"
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l

def save_letter(f:str,l:list):
    """Loetelu salvestame failisse
    """
    fail=open(f,"w")
    for el in l:
        fail.write(el+"\n")
    fail.close()

def read_file(f:str,l:list):
  fail=open(f,"r",encoding="utf-8-sig")
  mas=[]
  for line in fail:
    l.append(line.strip())
  fail.close()
  return l

def save_word(f:str,rida:str):
    """Üks sõna või lause(rida) salvestame failisse
    """
    fail=open(f,"a")
    fail.write(rida+"\n")
    fail.close()

def translate(l1:list,l2:list):
    slovo=input("Введите слово которое Вы хотите перевести -> ")
    if slovo in l1:
        trans=l2[l1.index(slovo)]
        print(slovo+" - "+ trans)
    elif slovo in l2:
        trans=l1[l2.index(slovo)]
        print(slovo+" - "+trans)
    else:
        print("К сожалению данное слово отсутcвует в списке.")
        print()
        print("Хотите ли Вы добавить вписанное слово в список?")
        print("1 - Да")
        print("2 - Нет")
        v=int(input("-> "))
        if v==1:
          new_word()
        if v==2:
          print("...")

def fail_save(f:str,l:list):
  fail=open(f,"w")
  for el in l:
    fail.write(el+"\n")
  fail.close

def correction(rus:list,ang:list,f1:list,f2:list):
  print("Введите слово которое было написано с ошибкой")
  word=input("-> ")
  if word not in rus and word not in ang:
    print("Написанное Вами слово отсутсвует в списке.")
  else:
    if word in rus:
      trans=ang[rus.index(word)]
      rus.remove(word)
      ang.remove(trans)
    elif word in ang:
      trans=rus[ang.index(word)]
      ang.remove(word)
      rus.remove(trans)
    rus.append(input("Введите исправленное слово ( на русском ) ->"))
    ang.append(input("Введите исправленное слово( на английском ) -> "))
    fail_save(f1,rus)
    fail_save(f2,ang)


def new_word():
    print("Введите слово на русском, которое Вы хотите добавить.")
    rusw=input("-> ")
    print("Введите слово на английском, которое Вы хотите добавить.")
    engw=input("-> ")
    rus=save_word("rus.txt",rusw)
    eng=save_word("ang.txt",engw)
    return rus, eng
    print("Ваше слово удачно добавлено!")

 import os
 from gtts import gtts

def heli(text:str,language:str):
   obj=gTTS(text=text,language=lang,slow=False).save("heli.mp3")
   os.system("heli.mp3")
