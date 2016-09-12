package ProjectEuler;

public class Problem_002 {
    public static void main(String[] args) {
        double start = System.nanoTime();

        int num1 = 1;
        int num2 = 2;
        int temp = 0;
        int sum = 0;

        while (num2 < 4_000_000) {
            if (num2 % 2 == 0) {
                sum += num2;
            }
            temp = num1 + num2;
            num1 = num2;
            num2 = temp;
        }
        System.out.println(sum);
        System.out.println((System.nanoTime() - start) / 1_000_000);
    }
}
