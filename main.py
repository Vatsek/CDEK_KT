with open('kt.csv', 'r', encoding="utf-8") as data:
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
