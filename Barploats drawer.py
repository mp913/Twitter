import matplotlib
import matplotlib.pyplot as plt

input_file = open("classifications.txt", 'r', encoding='UTF8')
for i in range(4):
    plt.figure(figsize=(20, 10))
    rule_label = input_file.readline()
    good_number = int(input_file.readline().split(" ")[2])
    bad_number = int(input_file.readline().split(" ")[2])
    normal_number = int(input_file.readline().split(" ")[2])
    labels = ['Good', 'Bad', 'Neutral']

    plt.xticks(range(3), labels)
    plt.title(rule_label)
    plt.xlabel('Tweet class')
    plt.ylabel('Number')
    plt.bar(range(3), [good_number, bad_number, normal_number], color=['green', 'red', 'blue'])
    plt.show()

    empty_line = input_file.readline()

plt.figure(figsize=(20, 10))
input_file = open("adjectives.txt", 'r', encoding='UTF8')
header = input_file.readline()
word = []
number = []
for i in range(5):
    tup = input_file.readline().split(' ')
    word.append(tup[0])
    number.append(int(tup[2]))

plt.subplot(1, 2, 1)
plt.title(header)
plt.xticks(range(5), word)
plt.ylabel('Number')
plt.bar(range(5), number, color='green')

empty_line = input_file.readline()

header = input_file.readline()
word = []
number = []
for i in range(5):
    tup = input_file.readline().split(' ')
    word.append(tup[0])
    number.append(int(tup[2]))

plt.subplot(1, 2, 2)
plt.title(header)
plt.xticks(range(5), word)
plt.ylabel('Number')
plt.bar(range(5), number, color='red')
plt.show()
