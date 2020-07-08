"""
python3 -m http.server - запуск хттп сервера на пайтон
python3 -m http.server 7800 - запустить на порту 7800



f = open('name file.py', 'w') - открыть файл для записи
f = open('name file.py', 'r') - открыть файл для чтения. Так же если не указывать режим
f = open('name file.py', 'a') - открыть файл для добавления

while True: - для чтения файла
    line = f.readline() - читает файл построчно
    if len(line) == 0: # Нулевая длина обозначает конец файла (EOF)
        break
    print(line, end='')

import pickle - позволяет сохранять любой ОБЪЕКТ PYTHON в файл. И доставать его обратно. 
f = open(shopelist, 'wb') - СНАЧАЛА open с WB - бинарной записью.
pickle.dump (shoplist, f)
shoplist = pickle.load(f)

"""