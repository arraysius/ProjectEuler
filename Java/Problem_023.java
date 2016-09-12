package ProjectEuler;

import java.util.HashSet;
import java.util.Set;

public class Problem_023 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        long limit = 28123;
        long sum = 0;

        Set<Long> abundant_nums = new HashSet<>();
        for (long i = 1; i <= limit; i++) {
            if (sumDivisors(i) > i) {
                abundant_nums.add(i);
            }

            boolean isAbundantSum = false;
            for (long j : abundant_nums) {
                if (abundant_nums.contains(i - j)) {
                    isAbundantSum = true;
                    break;
                }
            }
            if (!isAbundantSum) {
                sum += i;
            }
        }

        System.out.println(sum);

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static long sumDivisors(long n) {
        long total = 1;
        for (double i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                total += i + (n / i);
            }
        }
        if (Math.sqrt(n) == (int) Math.sqrt(n)) {
            total -= Math.sqrt(n);
        }
        return total;
    }
}