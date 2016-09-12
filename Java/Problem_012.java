package ProjectEuler;

public class Problem_012 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        for (int i = 1; i > 0; i++) {
            int tNum = (i * (i + 1)) / 2;
            int factors = 2;
            for (int j = 2; j < Math.sqrt((long) tNum); j++) {
                if (tNum % j == 0) {
                    factors += 2;
                }
                if (Math.sqrt(tNum) == Math.floor(Math.sqrt(tNum))) {
                    factors -= 1;
                }
            }
            if (factors > 500) {
                System.out.println(tNum);
                break;
            }
        }

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

}