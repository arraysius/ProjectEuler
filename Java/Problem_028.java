package ProjectEuler;

public class Problem_028 {

	public static void main(String[] args) {
		double start = System.nanoTime();

		int length = 1001;
		long num = length * length;
		long total = num;

		for (int i = length - 1; i > 1; i -= 2) {
			for (int j = 0; j < 4; j++) {
				num -= i;
				total += num;
			}
		}

		System.out.println(total);

		System.out.println((System.nanoTime() - start) / 1_000_000);
	}
}