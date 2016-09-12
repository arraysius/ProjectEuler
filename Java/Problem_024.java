package ProjectEuler;

import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

public class Problem_024 {

    private static String text;
    private static Set<Long> perms;

    public static void main(String[] args) {
        double start = System.nanoTime();

        text = "0123456789";
        perms = new LinkedHashSet<>();
        permutation(text);
        System.out.println(perms.toArray()[999999]);

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static int factorial(int n) {
        int fac = 1;
        for (long i = n; i > 1; i--) {
            fac *= i;
        }
        return fac;
    }

    private static void permutation(String str) {
        permutation("", str);
    }

    private static void permutation(String prefix, String str) {
        int n = str.length();
        if (n == 0) {
            perms.add(Long.parseLong(prefix));
        } else {
            for (int i = 0; i < n; i++)
                permutation(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1, n));
        }
    }
}