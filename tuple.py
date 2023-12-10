import timeit
list_time=timeit.timeit(stmt="[1,2,3,4]")
tuple_time=timeit.timeit(stmt="(1,2,3,4)")
print(list_time)
print(tuple_time)
x=(1,2,3,4)
print(x)


