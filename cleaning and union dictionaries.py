# part 1: clean digor-rus dict

# TODO: перевести все буквы 'æ' в дигор-англ слвар на буквы из дигор-русск слов
def cleaning_digor_eng():
    with open('Дигорско-английский.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))

    lines = list(map(lambda line: line.replace('æ', 'ӕ'), lines))

    with open('Дигорско-английский очищенный.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            if line.strip():
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
                if line.strip():
                    f.write(line + '\n')


def cleaning_pronouns():
    with open('Местоимения.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))

    with open('Местоимения очищенные.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            if line.strip():
                f.write(line.replace('æ', 'ӕ') + '\n')


class Lexeme:
    def __init__(self, lex, transl_en, gramm):
        self.lex = lex
        self.transl_en = transl_en
        self.gramm = gramm

    def __str__(self):
        return f'''{self.lex}\n{self.transl_en}\n{self.gramm}\n'''

    def __repr__(self):
        return f'''{self.lex}\n{self.transl_en}\n{self.gramm}\n'''


def find_lexem(lexems, word):
    for i in range(len(lexems)):
        if word in lexems[i].lex:
            return i
    return -1


osetin_alphabet = {'а': 1, 'ӕ': 2, 'б': 3, 'в': 4, 'г': 5, 'гъ': 6, 'д': 7, 'дж': 8, 'дз': 9, 'е': 10,
                   'ё': 11, 'ж': 12, 'з': 13, 'и': 14, 'й': 15, 'к': 16, 'къ': 17, 'л': 18, 'м': 19,
                   'н': 20, 'о': 21, 'п': 22, 'пъ': 23, 'р': 24, 'с': 25, 'т': 26, 'тъ': 27, 'у': 28,
                   'ф': 29, 'х': 30, 'хъ': 31, 'ц': 32, 'цъ': 33, 'ч': 34, 'чъ': 35, 'ш': 36, 'щ': 37,
                   'ъ': 38, 'ы': 39, 'ь': 40, 'э': 41, 'ю': 42, 'я': 43}


def words_comparator(word1, word2):
    ossetian_alphabet = "а ӕ б в г гъ д дж дз е ё ж з и й к къ л м н о п пъ р с т тъ у ф х хъ ц цъ ч чъ ш щ ъ ы ь э ю я"
    i1 = 0
    i2 = 0
    while i1 < len(word1) and i2 < len(word2):
        letter1 = word1[i1]
        letter2 = word2[i2]
        if i1 + 1 < len(word1) and word1[i1: i1 + 2] in ossetian_alphabet:
            letter1 = word1[i1: i1 + 2]
            i1 += 1
        if i2 + 1 < len(word2) and word2[i2: i2 + 2] in ossetian_alphabet:
            letter2 = word2[i2: i2 + 2]
            i2 += 1
        if ossetian_alphabet.index(letter1) < ossetian_alphabet.index(letter2):
            return -1
        elif ossetian_alphabet.index(letter1) > ossetian_alphabet.index(letter2):
            return 1
        i1 += 1
        i2 += 1
    if len(word1) < len(word2):
        return -1
    elif len(word1) > len(word2):
        return 1
    return 0


def union_dictionaries():
    lexems = []
    count_paired_words = 0
    all_ = 0
    with open('Дигорско-английский очищенный.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
        i = 0
        while i < len(lines):
            if '-lexeme' in lines[i]:
                lexems.append(Lexeme(
                    lex=[i.strip('/').strip('|').strip() for i in lines[i + 1].strip(' lex:').strip('.').split('.')],
                    # lex=[lines[i + 1].strip(' lex:').strip('').split('.')],
                    transl_en=lines[i + 5].strip(' transl_en:').strip(),
                    gramm=[i.strip() for i in lines[i + 6].strip(' gramm:').split(',')]
                ))
                if '' in lexems[-1].lex:
                    lexems[-1].lex = lexems[-1].lex.remove('')
                i += 6
            i += 1
    with open('Местоимения.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
        i = 0
        while i < len(lines):
            if '-lexeme' in lines[i]:
                lexems.append(Lexeme(
                    lex=[i.strip('/').strip('|').strip() for i in lines[i + 2].strip(' stem:').strip('.').split('.')],
                    transl_en=lines[i + 5].strip(' transl_en:').strip(),
                    gramm=[i.strip() for i in lines[i + 6].strip(' gramm:').split(',')]
                ))
                if '' in lexems[-1].lex:
                    lexems[-1].lex = lexems[-1].lex.remove('')
                i += 6
            i += 1

    with open('Дигорско-русский очищенный.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))

    with open('unioned dictionary.txt', 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            if lines[i].find('[') == -1:
                all_ += 1
                f.write(lines[i] + '\n')
                r = i + 1
                while r < len(lines) and lines[r].find('[') != -1:
                    if lines[r].strip():
                        f.write(lines[r] + '\n')
                    r += 1
                ind = find_lexem(lexems, lines[i])
                if ind != -1:
                    count_paired_words += 1
                    f.write('	[m1]')
                    for gr in lexems[ind].gramm[:-1]:
                        f.write(f'[p][i][c][com]{gr},[/com][/c][/i][/p]')
                    f.write(f'[p][i][c][com]{lexems[ind].gramm[-1]},[/com][/c][/i][/p]')
                    f.write('[/m]\n')
                    f.write(f'	[m1][trn]{lexems[ind].transl_en}[/trn][/m]\n')
                i = r
            else:
                i += 1
    # print(all_, 'all_')
    # print(count_paired_words, 'count_paired_words')
    # print(len(lexems), 'lexems')
    used_lexems = [False] * len(lexems)
    with open('unioned dictionary.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
        for i in range(len(lines)):
            if lines[i].find('[') == -1:
                ind = find_lexem(lexems, lines[i])
                if ind != -1:
                    used_lexems[ind] = True

    for i in range(len(lexems)):
        if not used_lexems[i]:
            ind = 0
            # lexems[i].lex
            error_list = []
            temp = lexems[i].lex
            if len(temp) > 1:
                error_list.append(lexems[i])
                continue
            r = 0
            while r < len(lines):
                if lines[r].find('[') == -1:
                    if words_comparator(temp, lines[r]) == -1:
                        ind = r
                        r += 1
                    else:
                        break
                else:
                    r += 1

            gram = '	[m1]'
            for gr in lexems[ind].gramm[:-1]:
                gram += f'[p][i][c][com]{gr},[/com][/c][/i][/p]'
            gram += f'[p][i][c][com]{lexems[ind].gramm[-1]}[/com][/c][/i][/p]' + '[/m]'
            trn = f'	[m1][trn]{lexems[ind].transl_en}[/trn][/m]'
            lines.insert(ind, lexems[i].lex)
            lines.insert(ind + 1, gram)
            lines.insert(ind + 2, trn)

    with open('unioned dictionary2.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)


# with open('Дигорско-русский очищенный.txt', 'r', encoding='utf-8') as f:
#     a = sum(map(lambda x: x.rstrip("\n").strip() == "", f.readlines()))
#     print(a)
# cleaning_digor_rus()
# with open('Дигорско-русский очищенный.txt', 'r', encoding='utf-8') as f:
#     a = sum(map(lambda x: x.rstrip("\n").strip() == "", f.readlines()))
#     print(a)
# with open('Местоимения.txt', 'r', encoding='utf-8') as f:
#     a = sum(map(lambda x: x.rstrip("\n").strip() == "", f.readlines()))
#     print(a)
# cleaning_pronouns()
# with open('Местоимения очищенные.txt', 'r', encoding='utf-8') as f:
#     c  = 0
#     for i in f.readlines():
#         if i.startswith(' stem:'):
#             if len(i.strip(' stem:').strip().split('.')) > 1:
#                 print(i)
#                 c += 1
#     print(c)
#
# with open('Дигорско-английский очищенный.txt', 'r', encoding='utf-8') as f:
#     c = 0
#     for i in f.readlines():
#         if i.startswith(' lex:'):
#             if len(i.strip(' lex:').strip().split('.')) > 1:
#                 print(i)
#                 c += 1
#     print(c)
# cleaning_digor_eng()
# print(1)
# cleaning_digor_rus()
# print(2)
# cleaning_pronouns()
# print(3)
# union_dictionaries()
# print(4)
# print('ӕ' < 'б')


# убрать запятую после последней грам категории