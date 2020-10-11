def smallest_multiple(end):
    is_small_mul = True
    div = 1
    tries = 0
    while is_small_mul:
        for i in range(1, end+1):
            if div % i == 0:
                tries += 1
                if tries == end:
                    return div
            else:
                tries = 0
                div += 1

print(smallest_multiple(20))
