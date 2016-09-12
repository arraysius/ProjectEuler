package ProjectEuler;

import java.math.BigInteger;

public class Problem_015 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        System.out.println(paths(20, 20));

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    // (a + b) C (a)
    // (a + b)! / (a!(b)!)

    private static BigInteger paths(long x, long y) {
        return factorial(x + y).divide(factorial(x).multiply(factorial(y)));
    }

    private static BigInteger factorial(long n) {
        BigInteger fac = BigInteger.ONE;
        for (long i = n - 1; i > 1; i--) {
            fac = fac.multiply(BigInteger.valueOf(i));
        }
        return fac;
    }
}