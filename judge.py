inp = open("frequency.txt", "r", encoding='UTF8')
outp = open("estimations.txt", "w", encoding='UTF8')

common_sense_flag = False

for line in inp:
    arr = line.split(' ')
    print(arr[0], file=outp, end=' ')
    if common_sense_flag:
        print(0, file=outp)
        continue
    if int(arr[2]) < 10:
        common_sense_flag = True
    print(arr[0])
    flag = input()
    if flag == '1':
        print(-1, file=outp)
        continue
    elif flag == '2':
        print(1, file=outp)
        continue
    else:
        print(0, file=outp)
        continue

