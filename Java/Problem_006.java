package ProjectEuler;

public class Problem_006 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        int limit = 100;
        int sum_of_sqaures = 0;
        int square_of_sums = 0;

        for (int i = 1; i <= limit; i++) {
            sum_of_sqaures += i * i;
        }

        for (int i = 1; i <= limit; i++) {
            square_of_sums += i;
        }
        square_of_sums = square_of_sums * square_of_sums;

        System.out.println(square_of_sums - sum_of_sqaures);

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

}
