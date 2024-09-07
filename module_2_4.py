numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primes = True
for i in numbers[1:]:
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_primes = False
            break
        is_primes = True
    if is_primes == True:
        primes.append(i)
    else:
        not_primes.append(i)
print(f'Primes: {primes}\n Not Primes: {not_primes}')


