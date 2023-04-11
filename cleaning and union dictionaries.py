# part 1: clean digor-rus dict

# TODO: перевести все буквы 'æ' в дигор-англ слвар на буквы из дигор-русск слов
def replacing():
    with open('Дигорско-английский.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))

    lines = list(map(lambda line: line.replace('æ', 'ӕ'), lines))

    with open('Дигорско-английский очищенный.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


# TODO: выкинуть нафиг из дигор-русск все ненужное
def cleaning_digor_rus():
    # print('	' == ' ')
    # return
    with open('Дигорско-русский.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))

    with open('Дигорско-русский очищенный.txt.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            if line.find('[') == -1 or \
                    'm1' in line and ('см.' in line or 'тж.' in line) or \
                    'm3' in line:
                f.write(line + '\n')


# TODO: к каждому слову из дигор-русск слов добавить перевод из дигор англ вместе со строками gram
def union_dictionaries():
    # [p][i][c][com] грамм категория
    pass

union_dictionaries()
