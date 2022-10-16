# Задача: предложить улучшения кода для четырёх уже решённых задач из семинаров №№2 - 5 
# Необходимо использовать: lambda, filter, map, zip, enumerate, list comprehension

# 1. Семинар 2. Задание 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def zad_2_2_was():

    N = int(input('Укажите число: '))
    summ = 1
    M = 1

    while (M < N + 1):
        summ = M * summ
        M = M + 1
        print(summ)

def zad_2_2_became():

    N = int(input('Укажите число: '))

    def mult(M, N):
        result = N
        while (M < N + 1):
            result = M * result
            M = M + 1
        return(result)
    
    bill = [mult(1, N) for N in range(1, N+1)]
    print(bill)


#zad_2_2_became()

# 2. Cеминар 5. Задание 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""

def zad_5_1_was():

    text = str(input('Введите текст: '))
    trigger = 'абв'
    text = text.split()
    result = []

    for i in range(len(text) - 1):
        if trigger not in text[i]:
            result.append(text[i])

    result = " ".join(result)
    print(result)

def zad_5_1_became():

    text = str(input('Введите текст: '))
    trigger = 'абв'
    text = text.split()
    result = ' '.join((filter(lambda s: trigger not in s, text)))
    print(result)

#zad_5_1_became()

# 3. Семинар 3. Задание 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def zad_3_1_was():
    bill = [2, 3, 5, 9, 3, 8]
    curr = len(bill)
    summ = 0

    if curr % 2 == 0:
        curr = curr - 1
    else:
        curr = curr - 2

    while curr >= 0:
        summ = summ + bill[curr]
        curr = curr - 2
    
    print(f'Сумма элементов, стоящих на нечетных позициях заданного списка, равна {summ}')

def zad_3_1_became():

    import random
    bill = [random.randrange(1, 15) for n in range(1,8)]
    print(bill)
    new_bill = [bill[i] for i in range(0, len(bill) - 1) if i%2==1]
    result = sum(new_bill)
    print(f'Сумма элементов, стоящих на нечетных позициях заданного списка, равна {result}')

#zad_3_1_became()

# 4. Семинар 4. Задача 4. Дана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

def zad_4_4_was():

    import random
    k = int(input('Укажите степень k:'))
    list_of_factor = []
    poly = str('X')
    holy = []
    temp = str
    j = k

    for i in range(k):
        list_of_factor.append(int(random.randrange(1, 101)))

    for i in range(j):
        if i == k - 1:
            temp = str(list_of_factor[i]) + poly
            holy.append(temp)
        else:
            temp = str(list_of_factor[i]) + poly + ('^') + str(j)
            holy.append(temp)
        j = j - 1
        

    result = str(holy[0]) + ' + '

    for i in range(1, k):
        if i == k - 1:
            result = str(result) + str(holy[i]) + str(' + ') + str(random.randrange(1, 101)) + str(' = 0 ')
        else:
            result = str(result) + str(holy[i]) + str(' + ')

    print(result)

    my_file = open("4_k_result.txt", "a+")
    my_file.write(result)
    my_file.close()

def zad_4_4_became():

    import random
    k = int(input('Укажите степень k:'))
    list_of_factor = [int(random.randrange(2, 101)) for k in range(1, k+2)]
    list_of_x = ['X' for k in range(1, k+1)]
    list_of_pow = ["^" + str(k) for k in range(k, 1, -1)]
    
    result_1 = list(zip(list_of_factor, list_of_x, list_of_pow))
    result_2 = str(list_of_factor[len(list_of_factor)-2]) + str(list_of_x[0])
    result_3 = str(list_of_factor[len(list_of_factor)-1])
    end_result = []

    for i in range(0, len(result_1)):
        end_result.append(str(result_1[i][0]) + str(result_1[i][1]) + str(result_1[i][2]))
    
    true_end_result = " + ".join(end_result) + " + " + result_2 + " + " + result_3 + " = 0"

    print(true_end_result) 

    my_file = open("4_k_result.txt", "a+")
    my_file.write(true_end_result)
    my_file.close()

zad_4_4_became()
