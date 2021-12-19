def read_file(input):
    arr = []
    with open(input, 'r') as f:
        for line in f.readlines():
            arr = list(map(int, line.split()))
    return arr


def min_array(input):
    arr = read_file(input)
    print("В файле:")
    print(*arr)
    print("Минимум:")
    minn = arr[0]
    for i in range(len(arr)):
        if minn < arr[i]:
            minn = arr[i]
    print(minn)


def max_array(input):
    arr = read_file(input)
    print("В файле:")
    print(*arr)
    print("Максимум:")
    maxx = arr[0]
    for i in range(len(arr)):
        if arr[i] > maxx:
            maxx = arr[i]
    print(maxx)


def sum_array(input):
    arr = read_file(input)
    print("В файле:")
    print(*arr)
    summ = 0
    for i in arr:
        summ += i
    print("Сумма:", summ)
    print()
    return summ


def mult_array(input):
    arr = read_file(input)
    print("В файле:")
    print(*arr)
    print("Произведение:")
    multt = 1
    for i in arr:
        multt *= i
    print(multt)


def write_file(input, arr):
    with open(input, 'w') as f:
        for i in arr:
            f.write(str(i) + "")
