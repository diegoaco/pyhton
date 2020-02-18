from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement

                    ### PERMUTATIONS ###

# Permuations of a set of size n without repetitions: n! outcomes 
per1 = [''.join(p) for p in permutations('abcd')]
print('Number of permutations: %d' %len(per1))
print('Outcomes:', per1)


# Permutations of lenght k of a set of size n without repetitions: n!/(n-k)! = n(n-1)(n-2)...(n-k+1) outcomes
per2 = [''.join(p) for p in permutations('abcd',2)]
print('Number of permutations: %d' %len(per2))
print('Outcomes:', per2)


# Permutations of lenght k of a set of size n (2 in this case) with repetitions: n^k outcomes
# This can model a coin toss, for example!
per3 = [''.join(p) for p in product('abc', repeat = 4)]
print('Number of permutations: %d' %len(per3))
print('Outcomes:', per3)


                    ### COMBINATIONS ###

# Combinations of lenght k of a set of size n: (n,k) = n!/[k!(n-k)!] outcomes

comb1 = [''.join(p) for p in combinations('abcd', 2)]
print('Number of combinations: %d' %len(comb1))
print('Combinations:', comb1)


# Combinations of lenght k of a set of size n with repetitions: (n+k-1)!/[k!(n-1)!] outcomes

comb2 = [''.join(p) for p in combinations_with_replacement('abcd',2)]
print('Number of combinations: %d' %len(comb2))
print('Outcomes:', comb2)


# Number of rearrangements (permutations) of the word 'STATISTICS' withouth duplicates

l = [''.join(p) for p in permutations('STATISTICS', 10)]
# Generating a set gets rid of duplicates:
s = set(l)
print('Number of arrangements: %d' %len(s))
