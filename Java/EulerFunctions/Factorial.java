package ProjectEuler.EulerFunctions;

import java.math.BigInteger;

public class Factorial {

    public static void main(String[] args) {
        double start = System.nanoTime();

        System.out.println(factorial(10));

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static BigInteger factorial(long n) {
        BigInteger fac = BigInteger.ONE;
        for (long i = n; i > 1; i--) {
            fac = fac.multiply(BigInteger.valueOf(i));
        }
        return fac;
    }
}