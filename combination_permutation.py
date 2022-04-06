#!/usr/bin/python3
def combination(length, *elements):
    """
    Generate elements combination

    example:
       Elements is ['a', 'b', 'c', 'd'], Combination length is 3
       Generate combinations is [['a', 'b', 'c'], ['a', 'b', 'd'], ['b', 'c', 'd']]

    :param length: one combination length
    :param elements: elements used for composition
    :return: combinations
    """
    if length <= 0:
        return []

    elif length >= len(elements):
        return list(elements)

    else:
        combinations = []
        indexes = [i for i in range(length)]
        elements_len = len(elements)

        while indexes[0] + length < elements_len:
            index_tail = len(indexes)-1
            while indexes[index_tail] < elements_len:
                
                combination_ele = []
                for index in indexes:
                    combination_ele.append(elements[index])
                combinations.append(combination_ele)

                indexes[index_tail] += 1

            indexes[index_tail] -= 1

            index_cur = index_tail
            length_relative = 0
            while index_cur > 0:
                if indexes[index_cur] + length_relative + 1 == elements_len:
                    if indexes[index_cur-1] + length_relative + 2 < elements_len:
                        indexes[index_cur-1] += 1

                index_cur -= 1
                length_relative += 1

            length_relative = length - 1
            for i in range(1, length):
                if indexes[i] + length_relative == elements_len:
                    indexes[i] = indexes[i - 1] + 1
                length_relative -= 1

        combination_ele = []
        for index in indexes:
            combination_ele.append(elements[index])
        combinations.append(combination_ele)

        return combinations


print(combination(3, 'a', 'b', 'c', 'd'))
