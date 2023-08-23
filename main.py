import csv
from glob import glob
import time

file = glob("*.csv")

if len(file) == 1:
    with open(file[0], 'r', encoding="utf-8") as data:
        for row in list(data)[0:1]:
            head = row.split(';')
            head_indx = []
            head_indx.append((head.index('Номер заказа')))
            head_indx.append((head.index('Статус')))
            head_indx.append((head.index('Контрольная точка')))
            head_indx.append((head.index('Дней в КТ')))
            head_indx.append((head.index('Тип')))
            head_indx.append((head.index('Причины задержки')))
            head_indx.append((head.index('Наличие СЗ')))
            head_indx.append((head.index('Наличие возвратной ведомости')))

        with open(file[0], 'r', encoding="utf-8") as data:
            result = []

            for line in data:
                new_list = []
                line_res = line.split(';') # список

                for i in head_indx:
                    new_list.append(line_res[i])

                tmp = ';'.join(new_list) # строка
                result.append(tmp) # в список записываем строку
    with open('kt_new.csv', 'w+', encoding='utf-8-sig') as data_new:
       result = map(lambda x: x + '\n', result)
       data_new.writelines(result)
       print("Complete!")
       time.sleep(0.5)
elif len(file) > 1:
    print("В папке находится больше одного файла CSV. Удалите лишние файлы и перезапустите программу")
    time.sleep(5)
    exit()
else:
    print("В папке нет ни одного файла CSV. Добавьте файл в папку и перезапустите программу")
    time.sleep(5)
    exit()
