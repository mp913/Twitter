import pymorphy2

inp = open("data.txt", "r", encoding='UTF8')
outp = open("clear_data.txt", "w", encoding='UTF8')
morph = pymorphy2.MorphAnalyzer()

#counter = int(0)
for line in inp:

    for s in ['!', '@', '$', '%', '^', '&', '*', '(', ')',
              '.', ',', '?', '-', '_', ';', '+', '=', ':',
              '"', '\n', '«', '»', '©', '/', "'", '\\', '0',
              '1', '2', '3', '4', '5', '6', '7', '8', '9',
              '<', '>', '[', ']']:
        line = line.replace(s, ' ')

    line = line.replace("RT ", "#")
    line = line.replace("# ", "#")
    input_string = line.split(" ")[2::]
    input_string = list(filter(lambda w: not w.startswith("#"), input_string))
    for word in input_string:

        word = word.lower()
        t = (morph.tag(word)[0]).POS
        if t in ['PREP', 'CONJ', 'PRCL', 'INTJ', None]:
            continue

        print(morph.parse(word)[0].normal_form + ' ', file=outp, end='')
    print('\n', file=outp)
    #counter += 1
    #if (counter == 30):
    #    exit(0)
