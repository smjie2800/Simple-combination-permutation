#!/usr/bin/python3
def combination(length, elements):
    """
    Generate elements combination

    example:
       Elements is ['a', 'b', 'c', 'd'], Combination length is 3
       Generate combinations is [['a', 'b', 'c'], ['a', 'b', 'd'], ['b', 'c', 'd']]

    :param length: one combination length
    :param elements: is list, used for composition. like ['a', 'b', 'c', 'd']
    :return: combinations
    """
    if length <= 0:
        return []

    elif length >= len(elements):
        return elements

    else:
        combinations = []
        indexes = [i for i in range(length)]
        elements_len = len(elements)
        index_tail = len(indexes) - 1

        while indexes[0] + length < elements_len:
            while indexes[index_tail] < elements_len:

                _combination = []
                for index in indexes:
                    _combination.append(elements[index])
                combinations.append(_combination)

                indexes[index_tail] += 1

            indexes[index_tail] -= 1
            index_cur = index_tail
            length_relative = 1
            while index_cur > 0:
                if indexes[index_cur] + length_relative == elements_len:
                    indexes[index_cur - 1] += 1

                    if indexes[index_cur - 1] + length_relative + 1 == elements_len:
                        _combination = []
                        for index in indexes:
                            _combination.append(elements[index])
                        combinations.append(_combination)

                index_cur -= 1
                length_relative += 1

            length_relative = length - 1
            for i in range(1, length):
                if indexes[i] + length_relative == elements_len:
                    indexes[i] = indexes[i - 1] + 1
                length_relative -= 1

        return combinations


def combination_sets(sets):
    """
    Generate sets's elements combination
    First generate every set's elements combination
    After generate final combinations using every set's elements combination

    example:
        sets: {"length": 2, "set": ['a1', 'a2', 'a3']}, {"length": 1, "set": ['b1', 'b2', 'b3']},
              {"length": 1, "set": ['c1', 'c2', 'c3']}
        First generate every set's elements combination: [['a1', 'a2'], ['a1', 'a3'], ['a2', 'a3']],
                                                         [['b1'], ['b2'], ['b3']], [['c1'], ['c2'], ['c3']]
        final combinations is ['a1', 'a2', 'b1', 'c1'], ['a1', 'a2', 'b1', 'c2'], ['a1', 'a2', 'b1', 'c3'],
                              ['a1', 'a2', 'b2', 'c1'], ['a1', 'a2', 'b2', 'c2'], ['a1', 'a2', 'b2', 'c3'], ...

    :param sets: is list, element contains one combination length and set,
                 set is list, used for composition. like ['a', 'b', 'c', 'd'].
                 like [{"length": 2, "set": ['a1', 'a2', 'a3']}, {"length": 1, "set": ['b1', 'b2', 'b3']}]
    :return:
    """
    combinations = []
    length = len(sets) + 1
    indexes = [0 for i in range(length)]
    combinations_set = [[] for i in range(length)]

    i = 1
    for _set in sets:
        combinations_set[i].extend(combination(_set.get("length"), _set.get("set")))
        i += 1

    index_tail = len(indexes) - 1
    combination_last_set_length = len(combinations_set[index_tail])

    while indexes[0] < 1:
        while indexes[index_tail] < combination_last_set_length:

            i = 1
            _combination = []
            for index in indexes[1:]:
                _combination.extend(combinations_set[i][index])
                i += 1
            combinations.append(_combination)

            indexes[index_tail] += 1

        indexes[index_tail] -= 1
        index_cur = index_tail
        while index_cur >= 0:
            if indexes[index_cur] + 1 == len(combinations_set[index_cur]):
                indexes[index_cur] = 0
            else:
                indexes[index_cur] += 1
                break

            index_cur -= 1

    return combinations


def permutation(length, elements):
    """
    Generate elements permutation

    example:
       Elements is ['a', 'b', 'c', 'd', 'e'], permutation length is 3
       Generate permutation is [['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'b', 'e'], ['a', 'c', 'b'], ['a', 'c', 'd'],
                               ['a', 'c', 'e']...]

    :param length: one permutation length
    :param elements: is list, used for permutation. like ['a', 'b', 'c', 'd', 'e']
    :return: permutations
    """
    if length <= 0:
        return []

    elif length >= len(elements):
        return elements

    else:
        permutations = []
        indexes = [0 for i in range(length+1)]
        values_set = [[] for i in range(length+1)]

        i = 0
        for values in values_set[1:]:
            values.extend(elements[i:])
            i += 1

        index_tail = len(indexes) - 1
        values_last_set_length = len(values_set[index_tail])

        while indexes[0] < 1:
            while indexes[index_tail] < values_last_set_length:

                i = 1
                _permutation = []
                for index in indexes[1:]:
                    _permutation.append(values_set[i][index])
                    i += 1
                permutations.append(_permutation)

                indexes[index_tail] += 1

            indexes[index_tail] -= 1
            index_cur = index_tail
            while index_cur >= 0:
                if indexes[index_cur] + 1 == len(values_set[index_cur]):
                    indexes[index_cur] = 0

                else:
                    indexes[index_cur] += 1

                    values_allow = elements.copy()
                    i = 1
                    for index in indexes[1:index_cur+1]:
                        values_allow.remove(values_set[i][index])
                        i += 1

                    for values in values_set[index_cur+1:]:
                        values.clear()
                        values.extend(values_allow)
                        values_allow.remove(values[0])

                    break

                index_cur -= 1

    return permutations
