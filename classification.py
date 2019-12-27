inp = open("clear_data.txt", "r", encoding='UTF8')
in_dict = open("estimations.txt", "r", encoding='UTF8')
outp = open("classifications.txt", "w", encoding='UTF8')

e_dictionary = dict()
for line in in_dict:
    arr = line.split(' ')
    e_dictionary[arr[0]] = int(arr[1])

e_dictionary['я'] = 0 # слово Я стоит в начале файла и при записи в словарь добавляется, как \uffefя

# классификация по первому правилу - сравнение суммы рейтингов с константами
f_writer = open("rule1.txt", "w", encoding='UTF8')
good_counter = 0
bad_counter = 0
normal_counter = 0

t_low = -1
t_up = 1
counter = 0
for line in inp:
    line = line.replace("\n", " ")
    if counter != 0:
        counter += 1
        counter %= 4
        continue
    counter += 1
    arr = line.split(' ')
    summ = 0
    for word in arr:
        if word in e_dictionary:
            summ += e_dictionary[word]
    if summ > t_up:
        print("1", file=f_writer)
        good_counter += 1
    if summ < t_low:
        print("-1", file=f_writer)
        bad_counter += 1
    if t_low <= summ <= t_up:
        print("0", file=f_writer)
        normal_counter += 1

counter = good_counter + bad_counter + normal_counter
print("Rule 1: sum of ratings", file=outp)
print("Good - " + str(good_counter) + " - " + str(round(100*good_counter/counter)) + "%", file=outp)
print("Bad - " + str(bad_counter) + " - " + str(round(100*bad_counter/counter)) + "%", file=outp)
print("Neutral - " + str(normal_counter) + " - " + str(round(100*normal_counter/counter)) + "%", file=outp)
print("", file=outp)

# классификация по второму правилу - сравнение долей типов слов
f_writer = open("rule2.txt", "w", encoding='UTF8')
good_counter = 0
bad_counter = 0
normal_counter = 0

inp = open("clear_data.txt", "r", encoding='UTF8')
counter = 0
for line in inp:
    line = line.replace("\n", " ")
    if counter != 0:
        counter += 1
        counter %= 4
        continue
    counter += 1
    arr = line.split(' ')

    good_word_counter = 0
    bad_word_counter = 0
    normal_word_counter = 0

    for word in arr:
        if word in e_dictionary:
            if e_dictionary[word] == -1:
                bad_word_counter += 1
            elif e_dictionary[word] == 1:
                good_word_counter += 1
            elif e_dictionary[word] == 0:
                normal_word_counter += 1

    if bad_word_counter > good_word_counter and bad_word_counter > normal_word_counter:
        print("-1", file=f_writer)
        bad_counter += 1
    elif good_word_counter > bad_word_counter and good_word_counter > normal_word_counter:
        print("1", file=f_writer)
        good_counter += 1
    else:
        print("0", file=f_writer)
        normal_counter += 1

counter = good_counter + bad_counter + normal_counter
print("Rule 2: percentage of ratings", file=outp)
print("Good - " + str(good_counter) + " - " + str(round(100*good_counter/counter)) + "%", file=outp)
print("Bad - " + str(bad_counter) + " - " + str(round(100*bad_counter/counter)) + "%", file=outp)
print("Neutral - " + str(normal_counter) + " - " + str(round(100*normal_counter/counter)) + "%", file=outp)
print("", file=outp)

# классификация по третьему правилу - обнаружили 3 или более положительных слов = твит хороший
good_counter = 0
bad_counter = 0
normal_counter = 0
f_writer = open("rule3.txt", "w", encoding='UTF8')

inp = open("clear_data.txt", "r", encoding='UTF8')
counter = 0
for line in inp:
    line = line.replace("\n", " ")
    if counter != 0:
        counter += 1
        counter %= 4
        continue
    counter += 1
    arr = line.split(' ')

    good_word_counter = 0
    bad_word_counter = 0
    normal_word_counter = 0

    for word in arr:
        if word in e_dictionary:
            if e_dictionary[word] == -1:
                bad_word_counter += 1
            elif e_dictionary[word] == 1:
                good_word_counter += 1
            elif e_dictionary[word] == 0:
                normal_word_counter += 1

    if good_word_counter > 2:
        print("1", file=f_writer)
        good_counter += 1
    elif bad_word_counter > good_word_counter:
        print("-1", file=f_writer)
        bad_counter += 1
    else:
        print("0", file=f_writer)
        normal_counter += 1

counter = good_counter + bad_counter + normal_counter
print("Rule 3: 3 good words", file=outp)
print("Good - " + str(good_counter) + " - " + str(round(100*good_counter/counter)) + "%", file=outp)
print("Bad - " + str(bad_counter) + " - " + str(round(100*bad_counter/counter)) + "%", file=outp)
print("Neutral - " + str(normal_counter) + " - " + str(round(100*normal_counter/counter)) + "%", file=outp)
print("", file=outp)

# классификация по четвертому правилу - хорошие - твиты без плохих слов, плозие - без хороших
good_counter = 0
bad_counter = 0
normal_counter = 0
f_writer = open("rule4.txt", "w", encoding='UTF8')

inp = open("clear_data.txt", "r", encoding='UTF8')
counter = 0
for line in inp:
    line = line.replace("\n", " ")
    if counter != 0:
        counter += 1
        counter %= 4
        continue
    counter += 1
    arr = line.split(' ')

    good_word_counter = 0
    bad_word_counter = 0
    normal_word_counter = 0

    for word in arr:
        if word in e_dictionary:
            if e_dictionary[word] == -1:
                bad_word_counter += 1
            elif e_dictionary[word] == 1:
                good_word_counter += 1
            elif e_dictionary[word] == 0:
                normal_word_counter += 1

    if bad_word_counter == 0:
        print("1", file=f_writer)
        good_counter += 1
    elif good_word_counter == 0:
        print("-1", file=f_writer)
        bad_counter += 1
    else:
        print("0", file=f_writer)
        normal_counter += 1

counter = good_counter + bad_counter + normal_counter
print("Rule 4: availability of good/bad words", file=outp)
print("Good - " + str(good_counter) + " - " + str(round(100*good_counter/counter)) + "%", file=outp)
print("Bad - " + str(bad_counter) + " - " + str(round(100*bad_counter/counter)) + "%", file=outp)
print("Neutral - " + str(normal_counter) + " - " + str(round(100*normal_counter/counter)) + "%", file=outp)
print("", file=outp)