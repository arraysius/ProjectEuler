package ProjectEuler;

public class Problem_004 {
    public static void main(String[] args) {
        double start = System.nanoTime();

        int largest = 0;
        for (int i = 999; i >= 0; i--) {
            for (int j = 999; j >= 0; j--) {
                int product = i * j;
                if (palindromeChecker(Integer.toString(product)) && product > largest){
                    largest = product;
                }
            }
        }

        System.out.println(largest);
        System.out.println((System.nanoTime() - start) / 1_000_000_000);
    }

    private static boolean palindromeChecker(String s) {
        String s_reverse = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            s_reverse += s.charAt(i);
        }

        return s.equals(s_reverse);
    }
}
