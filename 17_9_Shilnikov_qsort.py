def vvod_chisel():
    global string1
    string1 = input("Введите последовательность целых чисел через пробел:")
    proverka()

def proverka():
    global L
    try:
        L = list(map(int, string1.split()))
        qsort(L, 0, len(L)-1)
    except ValueError:
        print("Вводятся только целые числа через пробел, без использования разделяющих знаков")
        vvod_chisel()

def qsort(array, left, right):
    global L
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

def search(array, element, left, right):
    if L[left] <= element <= L[right]:
        middle = (right+left) // 2
        if array[middle] == element:
            print(f"Число находится на {middle+1} позиции списка")
            return middle
        elif element < array[middle]:
            if array[middle-1] < element:
                print(f"Число находится между {middle} и {middle+1} элементами списка")
            else:
                search(array, element, left, middle-1)
        else:
            if array[middle+1] > element:
                print(f"Число находится между {middle+1} и {middle+2} элементами списка")
            else:
                search(array, element, middle+1, right)
    else:
        print("Число не входит в список")

def pechat_spiska():
    print(L)

def vvod_chisla():
    global any_numb
    proverka_chisla()

def proverka_chisla():
    try:
        any_numb = int(input("Введите любое целое число:"))
        search(L, any_numb, 0, len(L) -1)
    except ValueError:
        print("Вводится только целое число")
        vvod_chisla()

vvod_chisel()
pechat_spiska()
vvod_chisla()






