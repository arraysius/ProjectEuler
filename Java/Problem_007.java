package ProjectEuler;

import java.util.ArrayList;
import java.util.List;

public class Problem_007 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        System.out.println(primeSieve(1_000_000));

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static int primeSieve(int limit) {
        // initially assume all integers are prime
        boolean[] isPrime = new boolean[limit];
        for (int i = 2; i < limit; i++) {
            isPrime[i] = true;
        }

        // mark non-primes < N using Sieve of Eratosthenes
        for (int i = 2; i * i < limit; i++) {

            // if i is prime, then mark multiples of i as non-prime
            // suffices to consider multiples i, i+1, ..., N/i
            if (isPrime[i]) {
                for (int j = i; i * j < limit; j++) {
                    isPrime[i * j] = false;
                }
            }
        }

        //Find 10_001st Prime
        int count = 0;
        for (int i = 2; i < limit; i++) {
            if (isPrime[i]) {
                count++;
            }

            if (count >= 10_001) {
                return i;
            }
        }
        return -1;
    }
}
