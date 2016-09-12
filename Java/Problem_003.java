package ProjectEuler;

import java.util.ArrayList;
import java.util.List;

public class Problem_003 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        long number = 600851475143L;
        List<Object> primes = primeSieve(10_000);
        String factors = "";

        for (int i = 0; i < primes.size(); i++) {
            int p = (int) primes.get(i);

            if (number % p == 0) {
                factors += p + " ";

                while (number % p == 0) {
                    number /= p;
                }
            }
        }

        System.out.println(factors);
        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static List<Object> primeSieve(int limit) {
        boolean[] numbers = new boolean[limit];
        for (int i = 2; i < limit; i++) {
            numbers[i] = true;
        }

        List<Object> primes = new ArrayList<>();

        for (int i = 0; i < limit; i++) {
            if (numbers[i]) {
                primes.add(i);

                for (int j = i * i; j < limit; j += i) {
                    numbers[j] = false;
                }
            }
        }

        return primes;
    }
}
