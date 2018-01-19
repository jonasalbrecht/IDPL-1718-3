    #include <stdio.h>
    #include <stdlib.h>
    #include <time.h>

    void findprimesupto(int n, int *primeslen, int *primes, int *n_primes) {
        int i, j, flag;

        *primeslen = 0;

        for (i=2; i <= n; i++) {
            for (j=0, flag=1; j < *primeslen; j++)
                if (n_primes[j] == i) {
                    flag = 0;
                    break;
                }
            if (flag) {
                primes[*primeslen] = i;
                n_primes[*primeslen] = i;
                (*primeslen)++;
            }
            for (j=0; j < *primeslen; j++)
                if (i > n_primes[j])
                    n_primes[j] += primes[j];
        }
    }

    int main() {
        int n = 10000, primeslen = 0, i;
        int *primes, *n_primes;
        clock_t start, diff;

        start = clock();
        primes = malloc(n * sizeof(int));
        n_primes = malloc(n * sizeof(int));

        findprimesupto(n, &primeslen, primes, n_primes);

        /* for (i=0; i < primeslen; i++)
            printf("%d ", primes[i]);

        printf("\n");
        */

        diff = clock() - start;
        printf("Time: %f s\n", (float) diff / (float) CLOCKS_PER_SEC);

        free(primes);
        free(n_primes);

        return 0;
    }
