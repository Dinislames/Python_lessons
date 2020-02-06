#kata 1
def scramble(s1,s2):
    diff = [0 for i in range(26)];
    for c in s1:
        diff[ord(c) - ord('a')] += 1;
    for c in s2:
        diff[ord(c) - ord('a')] -= 1;
    for i in range(26):
        if diff[i] < 0:
            return False;
    return True;

#Либо
from collections import Counter
def scramble(s1, s2):
    word = Counter(s1)
    word.subtract(s2)
    return not any(v < 0 for v in word.values())

#Вспоминаю все
mag = ['harry', 'misterio', 'huesos','librarians','fgvr']
for magic in mag:
    print(magic)

for value in range(1,5):
    print(value)

a = list(range(1,6))
b = list(range(2,13,2))
print(a)
print(b)
#генератор списка
squares = [value**2 for value in range(1,11)]
squr = [((value - 2)*2)**2 for value in range(1,11)];
print(squares)
print(squr)
#Срезы (slices)
new_squr = squr[0:3]
new_squr_2 = squr[3:]
print(new_squr)
print(new_squr_2)
#Копирование списка
tys = new_squr_2[:]
print(new_squr_2)
print(tys)

#tuples = immutable
dimension = (200,50,89,1)
print(dimension[0])
print(dimension [-1])
for value in dimension:
    print(value)

#if-if else - elif
mushrooms = ['onions','pepper','hvost','cheese']
print('onions' in mushrooms)
print('dsfd' in mushrooms)
#not in, для проверки отсутвия элемента в списке

#dictionary
alien_0 = {'color': 'green', 'potion': 5, 'planet': 'Hut'}
print(alien_0['color'])
print(alien_0['potion'])
alien_0['x-position'] = 25
alien_0['y-position'] = 0
for key,value in alien_0.items(): #alien_0.keys() and .valuse()
    print(key + " " + str(value));

#Задачки по курсу
objects = [1, 2, 1, 2, 3]
vault = set()
for object in objects:
    if id(object) not in vault:# что такое id() ???
        vault.add(id(object))
#print(len(vault))
#print(len(set(map(id, objects))))

def word_value(input_word):
    values = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    value = 0
    for letter in input_word:
        value += values[letter]
    return value

def high(x):
    list_words = x.split(" ")
    word_values = [word_value(word) for word in list_words]
    maximum = max(word_values)
    index = word_values.index(maximum)
    return list_words[index]

#print(high('take me to semynak'))

def diamond(n):
    if (n <= 1) or (n % 2 == 0):
        return None
    else:
        diamond_result = ''
        for i in range(n):
            # Определяем количество звездочек в строке
            if i <= n // 2:
                star = '*' * (i*2 + 1)
            else:
                star = '*' * ((n-i) * 2 - 1)
            # Формириуем строку, int(equation) - определение количества пробелов пред звездочкой, по сути центровка
            diamond_result += ' ' * ((n - len(star)) // 2) + star + '\n'
        return diamond_result
print(diamond(9))

def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    if lng < wdth:
        wdth, lng = lng, wdth
    res = []
    while lng != wdth:
        res.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            wdth, lng = lng, wdth
    res.append(wdth)
    return res
