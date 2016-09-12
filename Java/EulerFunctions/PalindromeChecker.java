package ProjectEuler.EulerFunctions;

public class PalindromeChecker {

    public static void main(String[] args) {
        double start = System.nanoTime();

        System.out.println(palindromeChecker("1001"));

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static boolean palindromeChecker(String s) {
        String s_reverse = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            s_reverse += s.charAt(i);
        }

        return s.equals(s_reverse);
    }

}
