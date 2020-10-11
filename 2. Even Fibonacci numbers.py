def fib_list(max_num=4000000):
    a, b, sequence = 1, 1, []
    while a < max_num:
        sequence.append(a)
        a, b = b, a+b
    return sequence


fib_array = fib_list()
total = 0
for num in fib_array:
    if num%2 == 0:
        total += num
print(total)

