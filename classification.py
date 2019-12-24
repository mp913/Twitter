import dostoevsky

inp = open("clear_data.txt", "r", encoding='UTF8')
in_dict = open("estimations.txt", "r", encoding='UTF8')
outp = open("classifications.txt", "w", encoding='UTF8')

e_dictionary = dict()
for line in in_dict:
    arr = line.split(' ')
    e_dictionary[arr[0]] = int(arr[1])

e_dictionary['я'] = 0 # слово Я стоит в начале файла и при записи в словарь добавляется, как \uffefя

# классификация по первому правилу - сравнение суммы рейтингов с константами
good_counter = 0
bad_counter = 0
normal_counter = 0

t_low = -1
t_up = 1
for line in inp:
    line = line.replace("\n", " ")
    if line == " ":
        continue
    arr = line.split(' ')
    summ = 0
    for word in arr:
        if word in e_dictionary:
            summ += e_dictionary[word]
    if summ > t_up:
        good_counter += 1
    if summ < t_low:
        bad_counter += 1
    if t_low <= summ <= t_up:
        normal_counter += 1

counter = good_counter + bad_counter + normal_counter
print("Rule 1: sum of ratings", file=outp)
print("Good - " + str(good_counter) + " - " + str(round(100*good_counter/counter)) + "%", file=outp)
print("Bad - " + str(bad_counter) + " - " + str(round(100*bad_counter/counter)) + "%", file=outp)
print("Neutral - " + str(normal_counter) + " - " + str(round(100*normal_counter/counter)) + "%", file=outp)
print("", file=outp)

# классификация по второму правилу - сравнение долей типов слов
good_counter = 0
bad_counter = 0
normal_counter = 0

inp = open("clear_data.txt", "r", encoding='UTF8')
for line in inp:
    line = line.replace("\n", " ")
    if line == " ":
        continue
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
        bad_counter += 1
    elif good_word_counter > bad_word_counter and good_word_counter > normal_word_counter:
        good_counter += 1
    else:
        normal_counter += 1

counter = good_counter + bad_counter + normal_counter
print("Rule 2: percentage of ratings", file=outp)
print("Good - " + str(good_counter) + " - " + str(round(100*good_counter/counter)) + "%", file=outp)
print("Bad - " + str(bad_counter) + " - " + str(round(100*bad_counter/counter)) + "%", file=outp)
print("Neutral - " + str(normal_counter) + " - " + str(round(100*normal_counter/counter)) + "%", file=outp)
print("", file=outp)