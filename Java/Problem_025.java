package ProjectEuler;

import java.math.BigInteger;

public class Problem_025 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        BigInteger a = BigInteger.ONE;
        BigInteger b = BigInteger.ONE;
        BigInteger temp;

        for (int i = 3; ; i++) {
            temp = a.add(b);
            a = b;
            b = temp;
            if (temp.toString().length() == 1000) {
                System.out.println(i);
                break;
            }
        }

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

}