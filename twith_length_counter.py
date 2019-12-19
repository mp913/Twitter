inp = open("clear_data.txt", "r", encoding='UTF8')
outp = open("twits_length.txt", "w", encoding='UTF8')

dictionary = dict()

for line in inp:
    arr = line.split(' ')
    if not(len(arr) - 1 in dictionary):
        dictionary[len(arr) - 1] = 1
    else:
        dictionary[len(arr) - 1] += 1;

summ = int(0)
for twith in dictionary:
    summ += dictionary[twith]

ans = []

for twith in dictionary:
    ans.append([dictionary[twith], str(twith) + " - " + str(dictionary[twith]) + " - " + str(round(100*dictionary[twith]/summ)) + "%"])

ans = sorted(ans, reverse=True)
ans = ans[1::]

for tup in ans:
    print(tup[1], file=outp)