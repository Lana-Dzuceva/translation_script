import openpyxl

# Открываем файл
workbook = openpyxl.load_workbook('murat sözlük.xlsx')

# Получаем активный лист
sheet = workbook.active
dic = {}
for row in sheet.iter_rows(min_row=2, values_only=True):
    key = row[0].replace('æ', 'ӕ').strip().strip('. -')
    val = row[1].replace('æ', 'ӕ').strip()
    if key in dic:
        dic[key].append(val)
    else:
        dic[key] = [val]
# TODO: объединить повторяющиеся слова
with open('turk-digor dictionary2.txt', 'w', encoding='utf-8') as f:
    for key, val in dic.items():
        f.write(key + '\n')
        f.write(f'''	[m1][trn]{'; '.join(val)}[/trn][/m]\n''')
        # print(row[0], row[1])
