"""USING THE INFINITE ITERATOR"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

#Count
print ("HASIL OUTPUT 1")
import itertools
for a, b in zip(range(3), itertools.count()):
    print (a, b)

print()
for a, b in zip(range(5, 8), itertools.count(5)):
    print (a, b)

#Cycle
print()
print ("HASIL OUTPUT 2")
for a, b in zip(range(5, 10, 2), itertools.count(5, 2)):
    print (a, b)

#Repeat
print()
print ("HASIL OUTPUT 3")
for a, b in zip(range(5, 10), itertools.count(5, 0.5)):
    print (a, b)
print()

"""USING THE FINITE ITERATOR"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

#Accumulate
import operator
import itertools

print ("HASIL OUTPUT ACCUMULATE")

#Accumulate
months = [10, 8, 5, 7, 12, 10, 5, 8, 15, 3, 4, 2]
print (list(itertools.accumulate(months, operator.add)))
print()

print ("HASIL OUTPUT CHAIN")

#Chain
a = range(3)
b = range(5)
print(list(itertools.chain(a, b)))
print()

print ("HASIL OUTPUT COMBINATIONS")

#Combinations
print(list(itertools.combinations(range(3), 2)))
print()
print(list(itertools.combinations_with_replacement(range(3), 2)))
print()

print ("HASIL OUTPUT PERMUTATIONS")

#Permutations
print(list(itertools.permutations(range(3), 2)))
print()

print ("HASIL OUTPUT COMPRESS")

#Compress
print(list(itertools.compress(range(1000), [0, 1, 1, 1, 0, 1])))

"""DROPWHILE() AND TAKEWHILE()"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

print ("HASIL OUTPUT DROPWHILE")

#Dropwhile
print(list(itertools.dropwhile(lambda x: x <= 3, [1, 3, 5, 4, 2])))
print()

print ("HASIL OUTPUT TAKEWHILE")

#TakeWhile
print(list(itertools.takewhile(lambda x: x <= 3, [1, 3, 5, 4, 2])))

"""GROUPBY()"""

print()
print ("Wifqi wifakul azmi")
print ("21102277")
print()

print ("HASIL OUTPUT GROUPBY")

#Groupby
items = [('a', 1), ('a', 2), ('b', 2), ('b', 0), ('c', 0)]
for group, items in itertools.groupby(items, lambda x: x[0]):
    print('%s: %s' % (group, [v for k, v in items]))
print()

#Groupby
items = [('a', 1), ('b', 0), ('b', 2), 
         ('a', 2), ('c', 3)]
groups = dict()
for group, items in itertools.groupby(items, lambda x: x[0]):
    groups[group] = items
    print('%s: %s' % (group, [v for k, v in items]))
print()