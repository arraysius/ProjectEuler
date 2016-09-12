package ProjectEuler.EulerFunctions;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PythagoreanTriplet {

    public static void main(String[] args) {
        double start = System.nanoTime();

        System.out.println(pythagoreanTriplet(100));

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static List pythagoreanTriplet(int limit) {
        List triplets = new ArrayList<>();
        for (int a = 1; a < limit; a++) {
            for (int b = a + 1; b < limit; b++) {
                double c = Math.ceil(Math.sqrt(Math.pow(a, 2.0) + Math.pow(b, 2.0)));
                if (Math.pow(a, 2.0) + Math.pow(b, 2.0) == Math.pow(c, 2.0)) {
                    triplets.add(Arrays.toString(new int[]{a, b, (int) c}));
                }
            }
        }
        return triplets;
    }
}
