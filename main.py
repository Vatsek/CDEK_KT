from glob import glob
import time

file = glob("*.csv")

if len(file) == 1:
    with open(file[0], 'r', encoding="utf-8") as data:
        result = []
        for line in data:
            new_list = []
            line_res = line.split(';')
            new_list.append(line_res[1])
            new_list.append(line_res[7])
            new_list.append(line_res[12])
            new_list.append(line_res[14])
            new_list.append(line_res[15])
            new_list.append(line_res[27])
            new_list.append(line_res[28])
            new_list.append(line_res[29])
            new_list.append(line_res[30])
            tmp = ';'.join(new_list)
            result.append(tmp)
    with open('kt_new.csv', 'w+', encoding='utf-8-sig') as data_new:
       result = map(lambda x: x + '\n', result)
       data_new.writelines(result)
       print("Complete!")
       time.sleep(1.5)
elif len(file) > 1:
    print("В папке находится больше одного файла CSV. Удалите лишние файлы и перезапустите программу")
    time.sleep(5)
    exit()
else:
    print("В папке нет ни одного файла CSV. Добавьте файл в папку и перезапустите программу")
    time.sleep(5)
    exit()
