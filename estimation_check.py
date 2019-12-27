in_dict = open("estimations.txt", "r", encoding='UTF8')

e_dictionary = dict()
for line in in_dict:
    arr = line.split(' ')
    e_dictionary[arr[0]] = int(arr[1])

e_dictionary['я'] = 0 # слово Я стоит в начале файла и при записи в словарь добавляется, как \uffefя

for i in range(1, 5):
    experiment_estimation_dictionary = dict()
    for key in e_dictionary:
        experiment_estimation_dictionary[key] = 0
    input_file = open("clear_data.txt", "r", encoding='UTF8')
    tweet_estimations = open("rule" + str(i) + ".txt", "r", encoding='UTF8')
    for line in input_file:
        if line == "\n":
            continue
        est = int(tweet_estimations.readline())
        line = line.replace("\n", "")
        words = line.split(" ")
        for word in words:
            if word in e_dictionary:
                experiment_estimation_dictionary[word] += est

    delta = list()
    for word in e_dictionary:
        delta.append([abs(experiment_estimation_dictionary[word]-e_dictionary[word]), word])

    delta = sorted(delta)
    output_file = open("estimation_check" + str(i) + ".txt", "w", encoding='UTF8')
    print("Top-5 Closest:", file=output_file)
    for j in range(5):
        print(delta[j][1] + " " + str(e_dictionary[delta[j][1]])
              + " " + str(experiment_estimation_dictionary[delta[j][1]]), file=output_file)

    print("", file=output_file)
    print("Top-5 Furthest:", file=output_file)
    for j in range(1, 6):
        print(delta[-j][1] + " " + str(e_dictionary[delta[-j][1]])
              + " " + str(experiment_estimation_dictionary[delta[-j][1]]), file=output_file)

    counter = 0
    bullseye_counter = 0
    for tup in delta:
        if abs(tup[0]) < 2:
            bullseye_counter += 1
        counter += 1

    print("", file=output_file)
    print("Estimation accuracy: " + str(round(bullseye_counter/counter * 100)) + "%", file=output_file)

###################################### most_positive_and_most_negative ######################################################

    experiment_estimation_results = list()
    for key in experiment_estimation_dictionary:
        experiment_estimation_results.append([experiment_estimation_dictionary[key], key])

    experiment_estimation_results = sorted(experiment_estimation_results)
    best_worst_output_file = open("best_worst" + str(i) + ".txt", "w", encoding='UTF8')
    print("Top-5 Most Positive:", file=best_worst_output_file)
    for j in range(1, 6):
        print(experiment_estimation_results[-j][1] + " " +
              str(experiment_estimation_results[-j][0]), file=best_worst_output_file)

    print("", file=best_worst_output_file)
    print("Top-5 Most Negative:", file=best_worst_output_file)
    for j in range(5):
        print(experiment_estimation_results[j][1] + " " +
              str(experiment_estimation_results[j][0]), file=best_worst_output_file)
