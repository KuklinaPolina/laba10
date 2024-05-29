def a10():
    import json
    def jsn():
        a = 'aa10.json'
        with open(a, 'r', encoding = 'aaaa') as b:
            d = json.load(b)

            for c in d['products']:
                print(f"Название: {c['name']} Цена: {c['price']}")
                print(f"Вес: {c['weight']}")
                if c['nal']:
                    print("В наличии")
                else:
                    print("Нет в наличии!")
        jsn()
def b10():
    import json
    import os

    a = r'C:\АиП\bb10.json'
    def b(product):
        if not os.path.exists(a):
            with open(a, 'w', encoding = 'aaaa') as f:
                json.dump({"products": []}, f, ensure_ascii = False)
        with open(a, 'r', encoding = 'aaaa') as f:
            d = json.load(f)
           d['products'].append(product)
        with open(a, 'w', encoding = 'aaaa') as f:
            json.dump(d, f, ensure_ascii = False, indent = 4)
    while True:
        name = input("Введите название продукта: ")
        price = int(input("Введите цену продукта: "))
        weight = int(input("Введите вес продукта: "))
        nal = input("Продукт в наличии?: ").lower() == 'да'

        product = {
            "name": name,
            "price": price,
            "weight": weight,
            "nal": nal}
        b(product)
        c = input("Хотите добавить еще продукт?: ").lower()
        if c != 'да':
            break
    with open('en-ru.txt', 'r') as f:
        l = f.readlines()
    ru_en_dict = {}
    for line in l:
        p = line.strip().split(' - ')
        if len(p) == 2:
            eng_word, ru_translations = p[0], p[1].split(',')
            for ru_word in ru_translations:
                ru_word = ru_word.strip()
                if ru_word in ru_en_dict:
                    ru_en_dict[ru_word].append(eng_word)
                else:
                    ru_en_dict[ru_word] = [eng_word]
    with open('ru-en.txt', 'w') as fy:
        for ru_word, eng_translations in ru_en_dict.items():
            fy.write(f"{ru_word} – {', '.join(eng_translations)}\n")
def c10():
    def cc10(fy, fu):
        ru_en = {}
        with open(fy, 'r') as f:
            for line in f:
                w = line.strip().split(' - ')
                if len(w) == 2:
                    en_w = w[0].strip()
                    ru_t = [ru.strip() for ru in w[1].split(',')]
                    for ru_w in ru_t:
                        ru_en[ru_w] = en_w
        c = sorted(ru_en.items())
        with open(fu, 'a') as fu:
            for ru_w, en_w in c:
                fu.write(f"{ru_w} – {en_w}\n")
    fy = 'Proba.txt'
    fu = 'ru-en.txt'
    cc10(fy, fu)