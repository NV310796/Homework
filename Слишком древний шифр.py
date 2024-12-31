import random
first_cell = random.choice(range(3, 21))
print('Число в первой вставке:', first_cell)
key0 = []
for digit1 in range(1, first_cell):
    for digit2 in range(1, first_cell):
        if first_cell % (digit1 + digit2) == 0:
            key0.append([digit1, digit2])


key1 = []
for i in key0:
    i.reverse()
    if i not in key1 and i.reverse() not in key1 and i[0] != i[1]:
        key1.append(i)


stroka = ''
for j in key1:
    stroka= stroka + ''.join(map(str, j))
key = int(stroka)
print('Число во вторую вставку:', key)

