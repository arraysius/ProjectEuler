package ProjectEuler;

public class Problem_014 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        long longest = 0;
        long number = 0;
        for (long i = 999_999; i > 1; i--) {
            long n = i;
            long chain = 1;
            while (n > 1) {
                if (n % 2 == 0) {
                    n /= 2;
                } else {
                    n = 3 * n + 1;
                }
                chain += 1;
            }
            if (chain > longest) {
                longest = chain;
                number = i;
            }
        }
        System.out.println(number);

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }
}