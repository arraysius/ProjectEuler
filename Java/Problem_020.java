package ProjectEuler;

import java.math.BigInteger;

public class Problem_020 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        String number = factorial(100).toString();
        long total = 0;
        for (int i = 0; i < number.length(); i++) {
            total += Character.getNumericValue(number.charAt(i));
        }
        System.out.println(total);

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static BigInteger factorial(long n) {
        BigInteger fac = BigInteger.ONE;
        for (long i = n - 1; i > 1; i--) {
            fac = fac.multiply(BigInteger.valueOf(i));
        }
        return fac;
    }
}