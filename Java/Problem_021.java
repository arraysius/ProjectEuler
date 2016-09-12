package ProjectEuler;

import java.util.ArrayList;
import java.util.List;

public class Problem_021 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        List<Integer> amicable_nums = new ArrayList<>();
        for (int a = 1; a < 10000; a++) {
            if (!checkPresent(a, amicable_nums)) {
                int b = d(a);
                if (a != b && d(b) == a) {
                    amicable_nums.add(a);
                    amicable_nums.add(b);
                }
            }
        }

        long sum = 0;
        for (int n : amicable_nums) {
            sum += n;
        }

        System.out.println(sum);
        System.out.println(amicable_nums);

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static int d(int n) {
        if (n == 1) {
            return 1;
        }
        int total = 1;
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

    private static boolean checkPresent(int n, List<Integer> amics) {
        for (int i : amics) {
            if (i == n) {
                return true;
            }
        }
        return false;
    }
}