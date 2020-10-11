def find_prime_factors(num):
    factors = []
    total = 1
    for i in range(1,num,2):
        if num % i == 0:
            for j in range(3,i,2):
                if i % j ==0:
                    for z in factors:
                        total *= z
                    if total == num:
                        print(f'{factors} is prime factors for {num}\n{factors[-1]} is the largiest')
                        return factors
            else:
                factors.append(i)


factors = find_prime_factors(600851475143)
