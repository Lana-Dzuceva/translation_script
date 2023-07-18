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
            if part.name in line:
                # part_of_speech.append(part.name)
                parts.append(part.name)
    return parts


def get_ref(lines):
    for line in lines:
        if ('q.v' in line or 'also' in line) and 'ref' in line:
            return line.split('ref]')[1]
    return ""


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
    ref = get_ref(dict_[word]['description'])
    if ref == "":
        return []
    c += 1
    return get_PoS(dict_, ref, c)


def to_string(word, dict_):
    if len(dict_[word]["description"]) > 0:
        return f'{word}\n  {dict_[word]["description"]}'
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
        'noun': open("noun.txt", 'w'),
        'pronoun': open("pronoun.txt", 'w'),
        'adjective': open("adjective.txt", 'w'),
        PartsOfSpeech.adverb.name: open("adverb.txt", 'w'),
        PartsOfSpeech.verb.name: open("verb.txt", 'w'),
        PartsOfSpeech.postposition.name: open("postposition.txt", 'w'),
        'indefinite words': open('indefinite words.txt', 'w'),
        'noun + adjective': open('noun + adjective.txt', 'w'),
        'adjective + adverb': open('adjective + adverb.txt', 'w'),
        'noun + adjective + adverb': open('noun + adjective + adverb.txt', 'w')
    }
    words_description = {}
    all_words = [''] * len(lines)
    c = 0
    i = 0
    while i < len(lines):
        cur_word = lines[i]
        all_words[c] = lines[i]
        c += 1
        i += 1
        words_description[cur_word] = {'part_of_speech': [],
                                       'description': []}
        while i < len(lines) and '[' in lines[i]:
            for part in PartsOfSpeech:
                if part.name in lines[i]:
                    words_description[cur_word]['part_of_speech'].append(part.name)
            words_description[cur_word]['description'].append(lines[i])
            i += 1
    for word in all_words:
        parts = get_PoS(word, words_description)
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


group_words_by_parts_of_speech()
