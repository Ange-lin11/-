def read_file(input):
    s1 = []
    with open(input, 'r') as f:
        for line in f.readlines():
            s1 += list(map(int, line.split()))
    return s1

def min_array(input):
    s2 = read_file(input)
    minn = s2[0]
    for i in range(len(s2)):
        if s2[i] < minn:
            minn = s2[i]
    print("В файле:")
    print(*s2)
    print("Минимальное: ", minn)
    print()
    return minn

def max_array(input):
    s2 = read_file(input)
    maxx = s2[0]
    for i in range(len(s2)):
        if s2[i] > maxx:
            maxx = s2[i]
    print("В файле:")
    print(*s2)
    print("Максимальное: ", maxx)
    print()
    return maxx

def sum_array(input):
    s2 = read_file(input)
    summa = 0
    for i in s2:
        summa += i
    print("В файле:")
    print(*s2)
    print("Сумма:", summa)
    print()
    return sum(s2)

def mult_array(input):
    s2 = read_file(input)
    mult = 1
    for i in s2:
        mult *= i
    if mult > 1000 ** 10:
        print("В файле:")
        print(*s2)
        print("Произведение:","Сумма слишком велика")
        print()
        return mult
    print("В файле:")
    print(*s2)
    print("Произведение:", mult)
    print()
    return mult

def sum_min_max_array(input):
    s2 = read_file(input)
    minn = s2[0]
    maxx = s2[0]
    for i in range(len(s2)):
        if s2[i] < minn:
            minn = s2[i]
    for j in range(len(s2)):
        if s2[j] > maxx:
            maxx = s2[j]
    summ2 = minn + maxx
    print("В файле:")
    print(*s2)
    print("Сумма минимального и максимального значения: ", summ2)
    print()
    return summ2

def write_file(input, s2):
    with open(input, 'w') as f:
        for i in s2:
            f.write(str(i) + " ")
