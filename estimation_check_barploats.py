import matplotlib
import matplotlib.pyplot as plt

for i in range(1, 5):
    best_worst_input_file = open("best_worst" + str(i) + ".txt", "r", encoding='UTF8')
    plt.figure(figsize=(20, 10))
    plt.subplot(1, 2, 1)
    best_label = best_worst_input_file.readline()

    labels = list()
    number = list()
    for j in range(5):
        tup = best_worst_input_file.readline().split(' ')
        labels.append(tup[0])
        number.append(float(tup[1]))

    plt.xticks(range(5), labels)
    plt.title(best_label)
    plt.ylabel('Number')
    plt.bar(range(5), number, color='green')

    empty_line = best_worst_input_file.readline()

    plt.subplot(1, 2, 2)
    best_label = best_worst_input_file.readline()

    labels = list()
    number = list()
    for j in range(5):
        tup = best_worst_input_file.readline().split(' ')
        labels.append(tup[0])
        number.append(float(tup[1]))

    plt.xticks(range(5), labels)
    plt.title(best_label)
    plt.ylabel('Number')
    plt.bar(range(5), number, color='red')

    plt.show()
