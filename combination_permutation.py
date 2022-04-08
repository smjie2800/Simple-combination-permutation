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

            is_complete = True
            length_relative = length
            for index in indexes:
                if index + length_relative != elements_len:
                    is_complete = False
                    break
                length_relative -= 1

            if is_complete:
                break

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
    length = len(sets)
    indexes = [0 for i in range(length)]
    combinations_set = [[] for i in range(length)]

    i = 0
    for _set in sets:
        combinations_set[i].extend(combination(_set.get("length"), _set.get("set")))
        i += 1

    print(combinations_set)

    combination_first_set_length = len(combinations_set[0])
    index_tail = len(indexes) - 1
    combination_last_set_length = len(combinations_set[index_tail])

    while indexes[0] < combination_first_set_length:
        while indexes[index_tail] < combination_last_set_length:

            i = 0
            _combination = []
            for index in indexes:
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

        is_complete = True
        for index in indexes:
            if index != 0:
                is_complete = False

        if is_complete:
            break

    return combinations


# print(len(combination(6, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])))
# print(combination_sets([{"length": 2, "set": ['a1', 'a2', 'a3']}, {"length": 1, "set": ['b1', 'b2', 'b3']},
#                         {"length": 1, "set": ['c1', 'c2', 'c3']}]))
























