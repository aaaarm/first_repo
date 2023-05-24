dict_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
dict_2 = {}

for value in dict_1.values():
    dict_2[value] = len(value)

print(dict_2)


def odd_numbers(d):
    dict_1 = {}

    for i, j in d.items():
        dict_2 = [x for x in j if x % 2 != 0]
        if dict_2:
            dict_1[i] = dict_2

    return dict_1


dict_3 = {'a': [1, 8, 3, 7, 2], 'b': [12, 4, 8, 4], 'c': [9, 9, 2, 8, 5]}
dict_4 = odd_numbers(dict_3)
print(dict_4)
