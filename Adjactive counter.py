import pymorphy2

in_dict = open("estimations.txt", "r", encoding='UTF8')
freq = open("frequency.txt", "r", encoding='UTF8')
outp = open("adjectives.txt", "w", encoding='UTF8')
morph = pymorphy2.MorphAnalyzer()

print("Top-5 Positive:", file=outp)
counter = 0
for line in in_dict:
    freq_line = freq.readline()
    arr = line.split(" ")
    t = (morph.tag(arr[0])[0]).POS
    if t in ["ADJF", "ADJS"] and arr[1] == "1\n":
        counter += 1
        print(freq_line, file=outp, end="")
        if counter == 5:
            break

print("", file=outp)
print("Top-5 Negative:", file=outp)
counter = 0
for line in in_dict:
    freq_line = freq.readline()
    arr = line.split(" ")
    t = (morph.tag(arr[0])[0]).POS
    if t in ["ADJF", "ADJS"] and arr[1] == "-1\n":
        counter += 1
        print(freq_line, file=outp, end="")
        if counter == 5:
            break