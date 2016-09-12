package ProjectEuler;

public class Problem_001 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        int sum = 0;
        for (int i = 1; i < 1_000_000; i++) {
            if (i % 3 == 0 || i % 5 == 0) {
                sum += i;
            }
        }
        System.out.println(sum);
        System.out.println((System.nanoTime() - start) / 1_000_000);
    }
}
