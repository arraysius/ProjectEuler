package ProjectEuler.EulerFunctions;

import java.util.ArrayList;
import java.util.List;

public class PrimeSieve {
    public static void main(String[] args) {
        double start = System.nanoTime();

        System.out.println(primeSieve(100));

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static List primeSieve(int limit) {
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

        // Collate Primes
        List primes = new ArrayList<>();
        for (int i = 2; i < limit; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }

        return primes;
    }
}