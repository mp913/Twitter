import pymorphy2

inp = open("data.txt", "r", encoding='UTF8')
outp = open("clear_data.txt", "w", encoding='UTF8')
morph = pymorphy2.MorphAnalyzer()

#counter = int(0)
for line in inp:

    for s in ['!', '@', '$', '%', '^', '&', '*', '(', ')', '.', ',', '?', '-', '_', ';', '+', '=', ':', '"', '\n', '«', '»']:
        line = line.replace(s, ' ')

    input_string = line.split(" ")
    RT_hashtag_flag = bool(False)
    for word in input_string:

        if RT_hashtag_flag:
            RT_hashtag_flag = False
            continue
        if word == "#" or word == "RT":
            RT_hashtag_flag = True
            continue

        word = word.lower()

        t = (morph.tag(word)[0]).POS
        if t in ['PREP', 'CONJ', 'PRCL', 'INTJ', None]:
            continue

        print(morph.parse(word)[0].normal_form + ' ', file=outp, end='')
    print('\n', file=outp)
    #counter += 1
    #if (counter == 30):
    #    exit(0)
