inp = open("clear_data.txt", "r", encoding='UTF8')
outp = open("frequency.txt", "w", encoding='UTF8')

dictionary = dict()

#counter = 0
for line in inp:
    arr = line.split(' ')
    for word in arr:
        if word == '\n':
            continue
        if not(word in dictionary):
            dictionary[word] = 0
        dictionary[word] = dictionary[word] + 1
    #if counter >= 40:
    #    break
    #counter += 1


summ = int(0)
for word in dictionary:
    summ += dictionary[word]

ans = []

for word in dictionary:
    ans.append([dictionary[word], word + " - " + str(dictionary[word]) + " - " + str(round(100*dictionary[word]/summ)) + "%"])

ans = sorted(ans, reverse=True)

for tup in ans:
    print(tup[1], file=outp)