def main():
    with open('глаголы.txt', 'r', encoding='utf-8') as f:
        lines = list(map(lambda x: x.rstrip("\n").replace('æ', 'ӕ'), f.readlines()))  # было еще .lower()
    with open('глаголы с формами.txt', 'w', encoding='utf-8') as f:
        for word in lines:
            f.write(word + '\n')
            if word in ' ':
                pass
            elif word[0] == 'æ':
                f.write('   ' + 'æр' + word + '\n')
                f.write('   ' + 'æрба' + word[1:] + '\n')
                f.write('   ' + 'ба' + word[1:] + '\n')
                f.write('   ' + 'ра' + word[1:] + '\n')
                f.write('   ' + 'фе' + word[1:] + '\n')
                f.write('   ' + 'ни' + word[1:] + '\n')
                f.write('   ' + 'ис' + word + '\n')
            elif word[0] in 'ае':
                f.write('   ' + 'æр' + word + '\n')
                f.write('   ' + 'æрбай' + word + '\n')
                f.write('   ' + 'бай' + word + '\n')
                f.write('   ' + 'рай' + word + '\n')
                f.write('   ' + 'фæйй' + word + '\n')
                f.write('   ' + 'нийй' + word + '\n')
                f.write('   ' + 'ис' + word + '\n')
            elif word[0] == 'и':
                f.write('   ' + 'æр' + word + '\n')
                f.write('   ' + 'æрбай' + word[1:] + '\n')
                f.write('   ' + 'бай' + word[1:] + '\n')
                f.write('   ' + 'рай' + word[1:] + '\n')
                f.write('   ' + 'фе' + word[1:] + '\n')
                f.write('   ' + 'ний' + word[1:] + '\n')
                f.write('   ' + 'ис' + word + '\n')
            else:
                f.write('   ' + 'æр' + word + '\n')
                f.write('   ' + 'æрба' + word + '\n')
                f.write('   ' + 'ба' + word + '\n')
                f.write('   ' + 'ра' + word + '\n')
                f.write('   ' + 'фæ' + word[0] + word + '\n')
                f.write('   ' + 'ни' + word[0] + word + '\n')
                f.write('   ' + 'ис' + word + '\n')
# print('ӕ' == 'æ')


main()
