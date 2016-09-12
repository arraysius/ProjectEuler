package ProjectEuler;

public class Problem_005 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        for (int i = 20; i > 0; i++) {
            boolean isDivisible = true;
            for (int j = 20; j > 0; j--) {
                if (i % j != 0) {
                    isDivisible = false;
                    break;
                }
            }

            if (isDivisible) {
                System.out.println(i);
                break;
            }
        }

        System.out.println((System.nanoTime() - start) / 1_000_000_000 + " s");
    }


}
