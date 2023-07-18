from enum import Enum


class PartsOfSpeech(Enum):
    noun = 1,
    pronoun = 2,
    adjective = 3,
    adverb = 4,
    verb = 5
    postposition = 6


def parse_parts_of_speech(lines):
    parts = []
    for line in lines:
        for part in PartsOfSpeech:
            if part.name in line.lower():
                # part_of_speech.append(part.name)
                parts.append(part.name)
    return parts


def get_ref(lines):
    for line in lines:
        if ('q.v' in line or 'also' in line) and 'ref' in line:
            return line.split('ref]')[1].rstrip('[/')
    return ""


def swap_case_fist_letter(word):
    if len(word) <= 1:
        return word.swapcase()
    return word[0].swapcase() + word[1:]

def get_PoS(word, dict_, c=0):
    """
    get part_of_speech of current word in this dictionary
    :param word:
    :param dict_:
    :param c:
    :return: list
    """
    if c > 8:
        return ["circle"]
    if len(dict_[word]['part_of_speech']) > 0:
        return dict_[word]['part_of_speech']
    elif len(dict_[word.lower()]['part_of_speech']) > 0:
        return dict_[word.lower()]['part_of_speech']
    ref = get_ref(dict_[word.lower()]['description'])
    if ref == "":
        return []
    c += 1
    return get_PoS(ref, dict_, c)


def get_PoS2(word, dict_, c=0):
    """
    get part_of_speech of current word in this dictionary
    :param word:
    :param dict_:
    :param c:
    :return: list
    """
    if c > 8:
        return ["circle"]
    if word in dict_ and len(dict_[word]['part_of_speech']) > 0:
        return dict_[word]['part_of_speech']
    elif word in dict_ and get_ref(dict_[word]['description']) != "":
        return get_PoS2(get_ref(dict_[word]['description']), dict_, c + 1)
    elif swap_case_fist_letter(word) in dict_ and len(dict_[swap_case_fist_letter(word)]['part_of_speech']) > 0:
        return dict_[swap_case_fist_letter(word)]['part_of_speech']
    if swap_case_fist_letter(word) in dict_:
        ref = get_ref(dict_[swap_case_fist_letter(word)]['description'])
        if ref == "":
            return []
        return get_PoS2(ref, dict_, c + 1)
    return []

def to_string(word, dict_):
    temp = '\n\t'
    if len(dict_[word]["description"]) > 0:
        return f'''{word}\n\t{temp.join(dict_[word]["description"])}\n'''
    return f'{word}\n'


def group_words_by_parts_of_speech():
    with open('ENG.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n").replace('æ', 'ӕ'), f.readlines()))  # было еще .lower()
    # nouns_file = open("noun.txt", 'w')
    # nouns_file = open("pronoun.txt", 'w')
    # nouns_file = open("adjective.txt", 'w')
    # nouns_file = open("adverb.txt", 'w')
    # nouns_file = open("verb.txt", 'w')
    # nouns_file = open("postposition.txt", 'w')
    files_to_write = {
        'noun': open("noun.txt", 'w', encoding='utf-8'),
        'pronoun': open("pronoun.txt", 'w', encoding='utf-8'),
        'adjective': open("adjective.txt", 'w', encoding='utf-8'),
        PartsOfSpeech.adverb.name: open("adverb.txt", 'w', encoding='utf-8'),
        PartsOfSpeech.verb.name: open("verb.txt", 'w', encoding='utf-8'),
        PartsOfSpeech.postposition.name: open("postposition.txt", 'w', encoding='utf-8'),
        'indefinite words': open('indefinite words.txt', 'w', encoding='utf-8'),
        'noun + adjective': open('noun + adjective.txt', 'w', encoding='utf-8'),
        'adjective + adverb': open('adjective + adverb.txt', 'w', encoding='utf-8'),
        'noun + adjective + adverb': open('noun + adjective + adverb.txt', 'w', encoding='utf-8')
    }
    words_description = {}
    all_words = []
    # c = 0
    i = 0
    while i < len(lines):
        cur_word = lines[i]
        all_words.append(lines[i])
        # c += 1
        i += 1
        if cur_word in words_description:
            print('All bed!')
        words_description[cur_word] = {'part_of_speech': [],
                                       'description': []}
        while i < len(lines) and '[' in lines[i]:
            for part in PartsOfSpeech:
                if part.name in lines[i].lower():
                    words_description[cur_word]['part_of_speech'].append(part.name)
            words_description[cur_word]['description'].append(lines[i])
            i += 1
    for word in all_words:
        parts = get_PoS2(word, words_description)
        if len(words_description[word]['part_of_speech']) == 0 and len(parts) > 0 and parts[0] != "circle":
            words_description[word]['part_of_speech'].extend(parts)

        if len(parts) == 1 and parts[0] != "circle":
            for part in PartsOfSpeech:
                if part.name in parts:
                    files_to_write[part.name].write(to_string(word, words_description))
        elif len(parts) == 0 or len(parts) == 1 and parts[0] == "circle":
            files_to_write['indefinite words'].write(to_string(word, words_description))
        elif PartsOfSpeech.noun.name in parts and PartsOfSpeech.adjective.name in parts:
            files_to_write['noun + adjective'].write(to_string(word, words_description))
        elif PartsOfSpeech.adjective.name in parts and PartsOfSpeech.adverb.name in parts:
            files_to_write['adjective + adverb'].write(to_string(word, words_description))
        elif PartsOfSpeech.noun.name in parts and PartsOfSpeech.adjective.name in parts and PartsOfSpeech.adverb.name in parts:
            files_to_write['noun + adjective + adverb'].write(to_string(word, words_description))

# print('Ӕ'.lower(), 'ӕ', 'Ӕ'.lower() == 'ӕ')
group_words_by_parts_of_speech()
