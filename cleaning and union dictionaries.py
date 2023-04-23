def cleaning_digor_eng():
    with open('Дигорско-английский.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n").lower().replace('æ', 'ӕ'), f.readlines()))
    # bad_letters = 'eyopakxc'
    # good_letters = 'еуоракхс'
    # for i in range(len(bad_letters)):
    #     lines = [i.replace(bad_letters[i], good_letters[i]) for i in lines]
    with open('Дигорско-английский очищенный.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            if line.strip():
                f.write(line + '\n')


def cleaning_digor_rus():
    # print('	' == ' ')
    # return
    with open('Дигорско-русский.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n").lower().replace('æ', 'ӕ'), f.readlines()))
    # bad_letters = 'eyopakxc'
    # good_letters = 'еуоракхс'
    # for i in range(len(bad_letters)):
    #     lines = [i.replace(bad_letters[i], good_letters[i]) for i in lines]
    with open('Дигорско-русский очищенный.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            if line.find('[') == -1 or \
                    'm1' in line and ('см.' in line or 'тж.' in line or 'мн.' in line) or \
                    'm3' in line:
                if line.strip():
                    f.write(line + '\n')


def cleaning_pronouns():
    with open('Местоимения.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n").lower().replace('æ', 'ӕ'), f.readlines()))
    # bad_letters = 'eyopakxc'
    # good_letters = 'еуоракхс'
    # for i in range(len(bad_letters)):
    #     lines = [i.replace(bad_letters[i], good_letters[i]) for i in lines]
    with open('Местоимения очищенные.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            if line.strip():
                f.write(line + '\n')


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
    try:
        ossetian_alphabet = " а ӕ б в г гъ д дж дз е ё ж з и й к къ л м н о п пъ р с т тъ у ф х хъ ц цъ ч чъ ш щ ъ ы ь э ю я"
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
    except Exception:
        if '-' not in word1 and '-' not in word2:
            print(word1, word2)
            print(Exception.args)
        if '-' in word1:
            return -1
        return 1


# print('c' == 'c')
# print(words_comparator("cтъона", 'дехгӕнӕг'))
# exit()

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
                    lex=[i.strip('/|').strip() for i in lines[i + 1].removeprefix(' lex:').strip('.').split('.')],
                    # lex=[lines[i + 1].strip(' lex:').strip('').split('.')],
                    transl_en=lines[i + 5].removeprefix(' transl_en:').strip(),
                    gramm=[i.strip() for i in lines[i + 6].removeprefix(' gramm:').split(',')]
                ))
                if '' in lexems[-1].lex:
                    lexems[-1].lex = lexems[-1].lex.remove('')
                i += 6
            i += 1
    with open('Местоимения очищенные.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
        i = 0
        while i < len(lines):
            if '-lexeme' in lines[i]:
                lexems.append(Lexeme(
                    lex=[i.strip('/|').strip() for i in lines[i + 2].removeprefix(' stem:').strip('.').split('.')],
                    transl_en=lines[i + 5].removeprefix(' transl_en:').strip(),
                    gramm=[i.strip() for i in lines[i + 6].removeprefix(' gramm:').split(',')]
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
                    f.write(f'[p][i][c][com]{lexems[ind].gramm[-1]}[/com][/c][/i][/p]')
                    f.write('[/m]\n')
                    f.write(f'	[m1][trn]{lexems[ind].transl_en}[/trn][/m]\n')
                i = r
            else:
                i += 1
    print(all_, 'all_')
    print(count_paired_words, 'count_paired_words')
    print(len(lexems), 'lexems')
    used_lexems = [False] * len(lexems)
    with open('unioned dictionary.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
        for i in range(len(lines)):
            if lines[i].find('[') == -1:
                ind = find_lexem(lexems, lines[i])
                if ind != -1:
                    used_lexems[ind] = True
    inserted = 0
    for i in range(len(lexems)):
        if not used_lexems[i]:
            inserted += 1
            ind = 0
            error_list = []
            temp = lexems[i].lex
            if len(temp) > 1:
                error_list.append(lexems[i])
                continue
            temp = temp[0]
            r = 0
            while r < len(lines):
                if lines[r].find('[') == -1:
                    if words_comparator(temp, lines[r]) == 1:
                        ind = r
                        r += 1
                    else:
                        break
                else:
                    r += 1
            # if ind == 0:
            #     print(temp)
            gram = '	[m1]'
            for gr in lexems[i].gramm[:-1]:
                gram += f'[p][i][c][com]{gr},[/com][/c][/i][/p]'
            gram += f'[p][i][c][com]{lexems[i].gramm[-1]}[/com][/c][/i][/p]' + '[/m]'
            trn = f'	[m1][trn]{lexems[i].transl_en}[/trn][/m]'
            lines.insert(ind, lexems[i].lex[0])
            lines.insert(ind + 1, gram)
            lines.insert(ind + 2, trn)
    print(inserted, "inserted")
    print(len(error_list), 'errorlist')
    with open('unioned dictionary2.txt', 'w', encoding='utf-8') as f:
        f.writelines([i + '\n' for i in lines])
    with open('errorlist.txt', 'w', encoding='utf-8') as f:
        f.writelines([i + '\n' for i in error_list])


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
# print(ord('æ'), ord('æ'))
# cleaning_digor_eng()
# print(1)
# cleaning_digor_rus()
# print(2)
# cleaning_pronouns()
# print(3)
# union_dictionaries()
# print(4)
# print('ӕ' < 'б')

def final_cleaning():
    with open('Английский.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))
    # print(len(lines))
    # i = 0
    # while i < len(lines):
    #     while i < len(lines) and not lines[i].strip():
    #         print(1)
    #         del lines[i]
    #     i += 1
    # print(len(lines))
    fixed_lines = []
    words_without_trn = []
    i = 0
    while i < len(lines):
        fixed_lines.append(lines[i])
        if i == len(lines) - 1 or '[' not in lines[i + 1]:
            words_without_trn.append(lines[i])
            i += 1
        else:
            i += 1
            temp = []
            while i < len(lines) and '[' in lines[i]:
                temp.append(lines[i])
                i += 1
            temp.sort()
            fixed_lines.extend(temp)

    with open('слова без перевода.txt', 'w', encoding='utf-8') as f:
        f.writelines([i + '\n' for i in words_without_trn])
    with open('Английский исправленный.txt', 'w', encoding='utf-8') as f:
        f.writelines([i + '\n' for i in fixed_lines])


def extract_word(s, start_ind, char_break):
    """
    не спрашивайте зачем она нужна. так надо
    :param s:
    :param start_ind:
    :param char_break:
    :return: слово и индекс, где остановились
    """
    temp = ''
    while s[start_ind] != char_break:
        temp += s[start_ind]
        start_ind += 1
    return temp.strip(), start_ind


def clear_string_m1():
    kw = ['см.', 'тж.', 'мн.']  # keywords
    with open('Английский исправленный.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.strip().rstrip("\n"), f.readlines()))
    with open('temp.txt', 'w', encoding='utf-8') as f:
        for i in range(len(lines)):
            line = lines[i]
            if 'm1' in line and kw[0] in line or kw[1] in line or kw[2] in line:
                dick = {
                    kw[0]: [],
                    kw[1]: [],
                    kw[2]: []
                }
                cur_kw = 0
                r = 0
                lenn = len(line)
                while r < lenn:
                    if line.startswith('[p][i][c][com]', r):
                        temp, r = extract_word(line, r + 14, '[')
                        r += 14  # minimum 10 forward
                        if temp in kw:
                            cur_kw = kw.index(temp)
                    if line.startswith('[ref]', r):
                        temp, r = extract_word(line, r + 5, '[')
                        r += 3
                        dick[kw[cur_kw]].append(temp)
                    # try: заигнорю слова на которые нет ссылок потому что он указывал только тег ref
                    #     if line.startswith('[i][com]', r) and not line.startswith('[i][com](', r):
                    #         temp, r = extract_word(line, r + 4, '')
                    #         dick[kw[cur_kw]].append(temp)
                    # except:
                    #     pass
                    if line.startswith('[i][com]([p][c]', r):
                        temp, r = extract_word(line, r + 15, '[')  # temp always == 'мн.'
                        r += 8
                        temp, r = extract_word(line, r, ')')
                        dick[kw[2]].append(temp)
                    r += 1
                part1 = ''
                if len(dick[kw[0]]) > 0:
                    part1 = f'[p][i][c][com]{kw[0]}[/com][/c][/i][/p] {", ".join([f"[ref]{ref}[/ref]" for ref in dick[kw[0]]])}'
                part2 = ''
                if len(dick[kw[1]]) > 0:
                    part2 = f'[p][i][c][com]{kw[1]}[/com][/c][/i][/p] {", ".join([f"[ref]{ref}[/ref]" for ref in dick[kw[1]]])}'
                part3 = ''
                if len(dick[kw[2]]) > 0:
                    part3 = f'[i][com]([p][c]{kw[2]}[/c][/p] {dick[kw[2]][0]})[/com][/i]'

                if len(part1) > 0 or len(part2) > 0 or len(part3) > 0:
                    line = f'[m1]{part1} {part2} {part3}[/m]'
                else:
                    continue
            if '[' in line:
                line = '	' + line
            while '  ' in line:
                line = line.replace('  ', ' ')
            f.write(line + '\n')


def testing():
    kw = ['см.', 'тж.', 'мн.']  # keywords
    with open('test.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.strip().rstrip("\n"), f.readlines()))
        for i in range(len(lines)):
            line = lines[i]
            # if line.count('.') > 1:
            #     print(line)
    with open('test_out.txt', 'w', encoding='utf-8') as f:
        for i in range(len(lines)):
            line = lines[i]
            if 'm1' in line and kw[0] in line or kw[1] in line or kw[2] in line:
                dick = {
                    kw[0]: [],
                    kw[1]: [],
                    kw[2]: []
                }
                cur_kw = 0
                r = 0
                lenn = len(line)
                while r < lenn:
                    if line.startswith('[p][i][c][com]', r):
                        temp, r = extract_word(line, r + 14, '[')
                        r += 14  # minimum 10 forward
                        if temp in kw:
                            cur_kw = kw.index(temp)
                    if line.startswith('[ref]', r):
                        temp, r = extract_word(line, r + 5, '[')
                        r += 2
                        dick[kw[cur_kw]].append(temp)
                    # try: заигнорю слова на которые нет ссылок потому что он указывал только тег ref
                    #     if line.startswith('[i][com]', r) and not line.startswith('[i][com](', r):
                    #         temp, r = extract_word(line, r + 4, '')
                    #         dick[kw[cur_kw]].append(temp)
                    # except:
                    #     pass
                    if line.startswith('[i][com]([p][c]', r):
                        temp, r = extract_word(line, r + 15, '[')  # temp always == 'мн.'
                        r += 8
                        temp, r = extract_word(line, r, ')')
                        dick[kw[2]].append(temp)
                    r += 1
                part1 = ''
                if len(dick[kw[0]]) > 0:
                    part1 = f'[p][i][c][com]{kw[0]}[/com][/c][/i][/p] {", ".join([f"[ref]{ref}[/ref]" for ref in dick[kw[0]]])}'
                part2 = ''
                if len(dick[kw[1]]) > 0:
                    part2 = f'[p][i][c][com]{kw[1]}[/com][/c][/i][/p] {", ".join([f"[ref]{ref}[/ref]" for ref in dick[kw[1]]])}'
                part3 = ''
                if len(dick[kw[2]]) > 0:
                    part3 = f'[i][com]([p][c]{kw[2]}[/c][/p] {dick[kw[2]][0]})[/com][/i]'

                if len(part1) > 0 or len(part2) > 0 or len(part3) > 0:
                    line = f'[m1]{part1} {part2} {part3}[/m]'
                else:
                    continue
            if '[' in line:
                line = '	' + line
            while '  ' in line:
                line = line.replace('  ', ' ')
            f.write(line + '\n')


def replace_m1():
    kw = ['см.', 'тж.', 'мн.']  # keywords
    with open('temp.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.strip().rstrip("\n"), f.readlines()))
    with open('temp2.txt', 'w', encoding='utf-8') as f:
        i = 0
        while i < len(lines):
            word = lines[i]
            r = i + 1
            space = '	'
            gr = []
            other = []
            trn = []
            m3 = []
            while r < len(lines) and '[' in lines[r]:
                if 'm3' in lines[r]:
                    m3.append(lines[r])
                elif 'trn' in lines[r]:
                    trn.append(lines[r])
                elif kw[0] in lines[r] or kw[1] in lines[r] or kw[2] in lines[r]:
                    other.append(lines[r])
                else:
                    gr.append(lines[r])
                r += 1

            i = r
            f.write(word + '\n')
            for m in other:
                f.write('	' + m + '\n')
            for m in gr:
                f.write('	' + m + '\n')
            for m in trn:
                f.write('	' + m + '\n')
            for m in m3:
                f.write('	' + m + '\n')


def transfer_duplicates():
    with open('temp2.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.strip().rstrip("\n"), f.readlines()))
    space = '	'
    used = []
    temp3_lines = []
    duplicated_lines = []
    i = 0
    while i < len(lines):
        word = lines[i]

        if word in used:
            duplicated_lines.append(word)
            r = i + 1
            while r < len(lines) and '[' in lines[r]:
                duplicated_lines.append(space + lines[r])
                r += 1
            i = r
        else:
            temp3_lines.append(word)
            r = i + 1
            while r < len(lines) and '[' in lines[r]:
                temp3_lines.append(space + lines[r])
                r += 1
            i = r
            used.append(word)

    with open('итоговый вариант.txt', 'w', encoding='utf-8') as f:
        for line in temp3_lines:
            f.write(line + '\n')
    with open('duplicated words.txt', 'w', encoding='utf-8') as f:
        for line in duplicated_lines:
            f.write(line + '\n')


transfer_duplicates()
# if 'см' in line or 'тж' in line:
#     sign = ''
#     refs = []
#     r = 0
#     while r < len(line):
#         if line[r] == 'p' and line[r:r + 13] == 'p][i][c][com]':
#             temp = ''
#             t = r + 13
#             while line[t] != '[':
#                 temp += line[t]
#                 t += 1
#             temp = temp.strip()
#             if temp in ['см', 'тж']:
#                 sign = temp
#         if line[r] == 'r' and line[r:r + 4] == 'ref]':
#             temp = ''
#             t = r + 4
#             while line[t] != '[':
#                 temp += line[t]
#                 t += 1
#             refs.append(temp)
#     line = f'	[m1][p][i][c][com]{sign}[/com][/c][/i][/p] {", ".join([f"[ref]{ref}[/ref]" for ref in refs])}[/m]'
# elif 'мн' in line:
#     pass
# line = line.removeprefix('[m1]').removesuffix('[/m]')
# line, ref = line[:line.find('[ref]')], line[line.find('[ref]'):]
# words = [''.strip(' ,.:|/;').removeprefix('[p][i][c][com]') for i in line.strip().split('[/com][/c][/i][/p]')]
# print(words)
# if i == 20:
#     return
# ref = ''
