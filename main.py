import json
with open("primer.json", "r", encoding='utf-8') as file: #преобразования сериализованного объекта в исходную структуру данных.
    f = json.load(file)
    for i in f:
        for j in f[i]:
            for x in j:
                if x == "name":
                    m = x.replace('name', 'Название')
                    print(m, j[x])
                if x == "price":
                    n = x.replace('price', 'Цена')
                    print(n, j[x])
                if x == "weight":
                    g = x.replace('weight', 'Вес')
                    print(g, j[x])
                if j[x] == True:
                    x = x.replace('available', 'В наличии')
                    print(x)
                else:
                    b = x.replace('available', 'Нет в наличии')
                    print(b)

def z11():
    with open('primer.json', 'r', encoding='utf-8') as f:
        file = json.load(f)  # загрузка содержимого файла в словарь

    for i in file['products']:
        print(f"Название: {i['name']}") #ключ меняется на "название" и значение итого ключа выводится
        print(f"Цена: {i['price']}")
        print(f"Вес: {i['weight']}")
        if i['available'] == True:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()

def z2():
    with open('primer.json', encoding='utf-8') as f:
        file = json.load(f)

    name = input("Введите название продукта: ")
    price = input("Введите цену продукта: ")
    weight = input("Введите вес продукта: ")
    available = input("Есть ли продукт в наличии?") == 'да'
    slovar = {"name": name, "price": price, "available": available, "weight": weight}
    file["products"].append(slovar) #добавление словаря в нач список
    with open('primer.json', 'w', encoding='utf-8') as f:
        json.dump(file, f)  # теперь этот список выше добавляем в наш начальный файл
    print()
    print("старое + добавленное :")
    print()

    with open('primer.json') as f: #снова проходимся по нашему файлику
        file = json.load(f) # словварь
        for i in file['products']:
            print(f"Название: {i['name']}")  # ключ меняется на название и значение итого ключа выводится
            print(f"Цена: {i['price']}")
            print(f"Вес: {i['weight']}")
            if i['available']:
                print("В наличии")
            else:
                print("Нет в наличии!")
            print()

def z3():
    with open('en-ru.txt', 'r', encoding='utf-8') as fi:
        spisok = fi.readlines() #строки  в 1 список
        print(spisok)
    ru_en = {}
    for i in spisok:
        e, r = i.strip().split(' - ')  # strip
        for rusword in r.split(','): #сплитим по запятой
            ru_en.setdefault(rusword.strip(), []).append(e.strip()) # setdefault добавляет в словарь : в ключ русское - ему англ в соответствие

    sort_slovar = dict(sorted(ru_en.items()))
    with open('ru-en.txt', 'w', encoding='utf-8') as f:
        for ru_word, en_words in sort_slovar.items():
            f.write(f"{ru_word} - {', '.join(en_words)}\n") # перезапись в новые строки с разделениями

z11()
z2()
z3()











