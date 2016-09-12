package ProjectEuler;

import java.math.BigInteger;

public class Problem_016 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        String number = new BigInteger("2").pow(1000).toString();
        long total = 0;
        for (int i = 0; i < number.length(); i++) {
            total += Character.getNumericValue(number.charAt(i));
        }
        System.out.println(total);

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

}