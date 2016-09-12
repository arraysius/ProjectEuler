package ProjectEuler;

public class Problem_017 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        String[] ones = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] tens_1x = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
        String[] tens = {"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

        long letters = 0;

        // 1 - 9
        for (int i = 1; i < 10; i++) {
            letters += ones[i - 1].length();
        }

        // 10 - 19
        for (int i = 10; i < 20; i++) {
            letters += tens_1x[i - 10].length();
        }

        // 20 - 99
        for (int i = 20; i < 100; i++) {
            letters += tens[i / 10 - 2].length();
            if (i % 10 != 0) {
                letters += ones[i % 10 - 1].length();
            }
        }

        // 100 - 999
        for (int i = 100; i < 1000; i++) {
            letters += ones[i / 100 - 1].length() + "hundred".length();
            if (i % 100 != 0) {
                letters += "and".length();
                if (i % 100 / 10 == 1) {
                    letters += tens_1x[i % 10].length();
                } else {
                    if (i % 100 / 10 != 0) {
                        letters += tens[i % 100 / 10 - 2].length();
                    }
                    if (i % 10 != 0) {
                        letters += ones[i % 10 -1].length();
                    }
                }
            }
        }
        
        letters += "onethousand".length();
        System.out.println(letters);

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

}