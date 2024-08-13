numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

numbers.remove(1)

for i in range(len(numbers)):
    a = numbers[i]
    for j in range(2, a):
        if a % j == 0:
            is_prime = False
            break
        else:
            is_prime = True

    if is_prime:
        primes.append(a)
    else:
        not_primes.append(a)

print('Primes: ',primes)
print('Not Primes: ', not_primes)
