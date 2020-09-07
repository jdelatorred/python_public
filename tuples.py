import sys
import timeit

#List example
prime_numbers = [2, 3, 5, 7, 11, 13, 17]

#tuple example
perfect_squares = (1, 2, 9, 16, 25, 36)

print("list methods:")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods:")
print(dir(perfect_squares))

#List occupied more memory than tuples

#List example
list1 = [128, True, "Alpha", 1.732, [64, False]]

tuple1 = (128, True, "Alpha", 1.732, [64, False])

print("List size = ", sys.getsizeof(list1))
print("Tuple size = ", sys.getsizeof(tuple1))

list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List Time: ", list_test)
print("Tuple Time: ", tuple_test)

empty_tuple =()
test1 = ("a",)
test2 = ("a","b")

print(empty_tuple)
print(test1)
print(test2)