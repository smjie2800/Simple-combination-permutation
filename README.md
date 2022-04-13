Introduction
=========================
This is a simple combination and permutation functions

#### Use Method

- use combination(length, elements) to generate combinations
  ```bash
  example:
      combination(3, ['a', 'b', 'c', 'd'])
      result: [['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'c', 'd'], ['b', 'c', 'd']]
  ```
- use combination_sets(sets) to generate sets combinations
  ```bash
  example:
      combination_sets([{"length": 2, "set": ['a1', 'a2', 'a3']}, {"length": 1, "set": ['b1', 'b2', 'b3']}, 
                        {"length": 1, "set": ['c1', 'c2', 'c3']}])
      result: [['a1', 'a2', 'b1', 'c1'], ['a1', 'a2', 'b1', 'c2'], ['a1', 'a2', 'b1', 'c3'], ['a1', 'a2', 'b2', 'c1'], 
              ['a1', 'a2', 'b2', 'c2'], ['a1', 'a2', 'b2', 'c3']...]
  ```
- use permutation(length, elements) to generate permutations
  ```bash
  example:
      permutation(3, ['a', 'b', 'c', 'd', 'e'])
  result:
      [['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'b', 'e'], ['a', 'c', 'b'], ['a', 'c', 'd'], ['a', 'c', 'e']...] 
  ```