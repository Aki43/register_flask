# 2)Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
# 1)Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key.
# Если и ключа 2 * key нет, то нужно добавить ключ 2 * key в словарь
# и сопоставить ему список из переданного элемента [value].
key = 2
value = 6
d = {}


def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)

    elif 2 * key in d:
        d[2 * key].append(value)

    else:
        d[2 * key] = []
        d[2 * key].append(value)

    print(d)


update_dictionary(d, key, value)
# dictionary[key]=value
