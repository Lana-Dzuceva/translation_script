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

    with open('Дигорско-русский очищенный.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            if line.find('[') == -1 or \
                    'm1' in line and ('см.' in line or 'тж.' in line or 'мн.' in line) or \
                    'm3' in line:
                f.write(line + '\n')


class Lexeme:
    def __init__(self, stem, transl_en, gramm):
        self.stem = stem
        self.transl_en = transl_en
        self.gramm = gramm

    def __str__(self):
        return f'''{self.stem}\n{self.transl_en}\n{self.gramm}\n'''

    def __repr__(self):
        return f'''{self.stem}\n{self.transl_en}\n{self.gramm}\n'''

def find_lexem(lexems, word):
    for i in range(len(lexems)):
        if word in Lexeme(lexems[i]).stem:
            return i
    return -1


# TODO: к каждому слову из дигор-русск слов добавить перевод из дигор англ вместе со строками gram
def union_dictionaries():
    # [p][i][c][com] грамм категория
    # для начала распарсю словарь в массив лексем
    lexems = []
    with open('Дигорско-английский очищенный.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
        i = 0

        while i < len(lines):
            if '-lexeme' in lines[i]:
                lexems.append(Lexeme(
                    stem=[i.strip('/').strip('|') for i in lines[i + 2].strip(' stem:').strip('.').split('.')],
                    transl_en=lines[i + 5].strip(' transl_en:').strip(),
                    gramm=[i.strip() for i in lines[i + 6].strip(' gramm:').split(',')]
                ))
                i += 6
            i += 1
        # for lexem in lexems[:50]:
        #     print(lexem)
    with open('Дигорско-русский очищенный.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
    with open('unioned dictionary.txt', 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            if lines[i].find('[') == -1:
                f.write(lines[i] + '\n')
                r = i + 1
                while lines[r].find('[') != -1:
                    f.write(lines[r] + '\n')
                ind = find_lexem(lexems, lines[i])
                if ind != -1:
                    for gr in lexems[ind]:
                        f.write()


        for line in lines:
            if line.find('[') == -1 or \
                    'm1' in line and ('см.' in line or 'тж.' in line or 'мн.' in line) or \
                    'm3' in line:
                f.write(line + '\n')


cleaning_digor_rus()
# union_dictionaries()
