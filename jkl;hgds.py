import math
'Урок №11. Функции'
'Задание №1'
'Создайте функцию, которая принимает в качестве параметра - натуральное целое число.'
'Данная функция находит факториал полученного числа'
'Например, факториал числа 3 это число 6.'
'Теперь создайте список факториалов чисел от получившегося ранее факториала 6, до 1.'
'В итоге, на вход программа получает например число 3, возвращает число 6 (факториал числа 3) и вам нужно сделать список из факториалов числа 6 в убывающем порядке.'
'Находим факториал числа 6 - это 720, затем от числа 5 - это 120 и так далее вплоть до 1'
'То есть, результирующий список будет выглядеть в нашем примере так: '
'[720, 120, 24, 6, 2, 1]'
def factorial(number):
    g=[]
    factorial=math.factorial(number)
    for i in range(factorial):
        gg=math.factorial(factorial)
        factorial-=1
        g.append(gg)
    print(g)

n1=int(input())
factorial(n1)





Задание 2


def age(vozrast_pitom):
    if vozrast_pitom % 10 == 1 and vozrast_pitom % 100 != 11:
        return    vozrast_pitom,"год"
    elif vozrast_pitom % 10 in [2, 3, 4] and not (vozrast_pitom % 100 in [12, 13, 14]):
        return    vozrast_pitom,"года"
    else:
        return    vozrast_pitom,"лет"
pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": age(9),
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": age(19),
                "Имя владельца": "Саша"
            },
        },
}
def create():
    global pets
    klich = input("введите кличку питомца:")
    vid_pitom = input("введите вид питомца")
    vozrast_pitom = int(input('введите его возраст'))
    imya_vald = input("введите имя владельца:")
    a = pets.keys()
    list(a)
    a = len(a) +1
    print(a)
    d=    {3:
        {
            klich: {
                "Вид питомца": vid_pitom,
                "Возраст питомца": age(vozrast_pitom),
                "Имя владельца": imya_vald
            },
        },
    }
    pets.update(d)
    print(pets)
def read():
    global pets
    n=int(input("введите id питомца о котором хотите узнать :  "))
    print(pets[n])
    if n not in pets:
        print("вы ввели некоректное id")
def update():
    global pets
    n1= int(input("введите id питомца данные о котором хотите изменить"))
    if n1 in pets:
        klich = input("введите кличку питомца:")
        vid_pitom = input("введите вид питомца")
        vozrast_pitom = int(input('введите его возраст'))
        imya_vald = input("введите имя владельца:")
        a = pets.keys()
        list(a)
        a = len(a)
        print(a)
        d=    {a:
            {
                klich: {
                    "Вид питомца": vid_pitom,
                    "Возраст питомца": vozrast_pitom,
                    "Имя владельца": imya_vald
                },
            },
        }
    pets.update(d)
    print(pets)
def delete():
    global pets
    n1=int(input("выберите id питомца которого надо удалить из списка"))
    if n1 in pets:
        del pets[n1]

    else:print("вы ввели некорректный id")
def Bce_pitom():
    print(pets)

while True:
    command=int(input("приветствуем вас в нашей поликлинике ,,Дохлый кот'' \n "
                  "вы хотите создать анкету о пете если да то нажмите 1 \n"
                  "если вы хотите просмотреть существующую анкету нажмите 2\n"
                  "eсли вы хотите обновить инфу о пете нажмите 3 \n"
                  "если хотите удалить запись о пете нажмите 4 \n"
                   "если хотите вывести информацию сразу о всех животных 5\n"
                  "если хотите завершить текущий сеанс нажмите 6"))
    if command==1:
        create()
    elif command==2:
        read()
    elif command==3:
        update()
    elif command==4:
        delete()
    elif command==5:
        Bce_pitom()
    elif command==6:
        break



