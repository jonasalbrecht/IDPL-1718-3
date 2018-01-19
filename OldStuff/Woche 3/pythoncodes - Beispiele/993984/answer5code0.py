def findprimeupto(x):
    primes = []
    n_primes = []

    for i in range(2, x):

        if not (i in n_primes):
            primes.append(i)
            n_primes.append(i)

        for j in range(len(primes)):
            if i > n_primes[j]:
                n_primes[j] += primes[j]

    return primes

import time
start_time = time.time()
findprimeupto(10000)
print("--- %s seconds ---" % str(time.time() - start_time))
