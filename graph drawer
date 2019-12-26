import matplotlib.pyplot as plt

scale = 20
x_legend_scale = 4
x_datetime = []
y_tweet_amount = []

for i in range(1, 5):
    input_filename = "hours" + str(i) + ".txt"
    input_file = open(input_filename, "r", encoding='UTF8')
    x_datetime = []
    y_good = []
    y_normal = []
    y_bad = []
    y_tweet_amount = []
    for line in input_file:
        tup = line.split(" ")
        y_tweet_amount.append(int(tup[6]))
        proportion = tup[7].split("/")
        x_datetime.append(tup[4] + "\n" + tup[3])
        y_good.append(float(proportion[0]))
        y_normal.append(float(proportion[1]))
        y_bad.append(float(proportion[2]))

    x_datetime = x_datetime[::scale]
    y_good = y_good[::scale]
    y_bad = y_bad[::scale]
    y_normal = y_normal[::scale]
    y_tweet_amount = y_tweet_amount[::scale]
    x_invisible_datetime = []

    for i in range(0, len(x_datetime)):
        x_invisible_datetime.append(" " * i)
        if i % x_legend_scale != 0:
            x_datetime[i] = " " * i

    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(2, 1, 1)
    ax.plot(x_invisible_datetime, y_good, alpha=0.7, label="N_pos", color='r', marker='o', markevery=1)
    ax.plot(x_invisible_datetime, y_normal, alpha=0.7, label="N", color='g', marker='o', markevery=1)
    ax.plot(x_invisible_datetime, y_bad, alpha=0.7, label="N_neg", color='b', marker='o', markevery=1)
    ax.set_ylabel(ylabel="Fraction")
    ax.legend()
    ax.grid(True)
    ax = fig.add_subplot(2, 1, 2)
    ax.grid(True)
    ax.stem(x_datetime, y_tweet_amount, label="Number of tweets", basefmt="None")
    ax.set_xlabel('Time window')
    ax.set_ylabel('Number of tweets')
    plt.show()
