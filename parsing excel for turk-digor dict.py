import openpyxl

# Открываем файл
workbook = openpyxl.load_workbook('murat sözlük.xlsx')

# Получаем активный лист
sheet = workbook.active
# print(sheet)


with open('turk-digor dictionary.txt', 'w', encoding='utf-8') as f:
    for row in sheet.iter_rows(min_row=2, values_only=True):
        f.write(row[0].replace('æ', 'ӕ') + '\n')
        f.write(f'''	[m1][trn]{row[1].replace('æ', 'ӕ')}[/trn][/m]\n''')
        # print(row[0], row[1])
