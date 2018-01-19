import numpy

def findprimeupto(x):

    primes = numpy.array(numpy.zeros(x), dtype=numpy.int32)
    n_primes = numpy.array(numpy.zeros(x), dtype=numpy.int32)
    primeslen = 0

    for i in range(2, x):

        flag = 1
        for j in range(primeslen):
            if n_primes[j] == i:
                flag = 0
                break

        if flag:
            primes[primeslen] = i
            n_primes[primeslen] = i
            primeslen += 1

        for j in range(primeslen):
            if i > n_primes[j]:
                n_primes[j] += primes[j]

    return [primeslen, primes]


import time

start_time = time.time()

result = findprimeupto(10000)

#for i in range(result[0]):
#    print('{:d} '.format(result[1][i]), end="")

print()
print("--- %s seconds ---" % str(time.time() - start_time))
