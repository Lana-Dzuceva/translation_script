from re import Match, sub
import requests
import re

path = f'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=tr&dt=t&q='
pref = " transl_tr: "
with open('digor.txt', 'r', encoding='utf-8') as f:
    lines = list(map(lambda x: x.rstrip("\n"), f.readlines()))

replaces_before = ["etc\.",
                   "smb\.",
                   "smth\.",
                   "e\.g",
                   "i\.e",
                   "smb's",
                   "etc",
                   "smb",
                   "smth"
                   ]
replaces_after = ["and so on",
                  "somebody",
                  "something",
                  "for example",
                  "that is to say",
                  "somebody's",
                  "and so on",
                  "somebody",
                  "something"
                  ]

with open('updated_file.txt', 'a', encoding='utf-8') as f:
    c = 0
    for line in lines:
        f.write(line + '\n')
        if line.startswith(" transl_en:"):
            c += 1
            print(c)
            prepared_line = line.removeprefix(" transl_en: ")
            translation = ""
            if prepared_line and prepared_line.strip():
                for i in range(len(replaces_before)):
                    prepared_line = sub(r'\b{0}\b'.format(replaces_before[i]), replaces_after[i], prepared_line)
                req = requests.get(path + prepared_line).json()[0]
                translation = ''.join(map(lambda x: x[0], req))

            f.write(pref + translation + '\n')

# def findWholeWord(w):
#     return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

# re.search(r'\b{0}\b'.format(line_to_replace), line)
# words_to_translate = re.split('; |, ', line.removeprefix(" transl_en: "))
