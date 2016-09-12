package ProjectEuler;

public class Problem_019 {

    public static void main(String[] args) {
        double start = System.nanoTime();

        int weekday = 1;
        long count = 0;
        for (int year = 1901; year <= 2000; year++) {
            boolean leap = isLeap(year);
            for (int month = 1; month <= 12; month++) {
                int days = daysInMonth(month, leap);
                if (weekday == 6) {
                    count++;
                }
                weekday = (weekday + days) % 7;
            }
        }
        System.out.println(count);

        System.out.println((System.nanoTime() - start) / 1_000_000 + " ms");
    }

    private static boolean isLeap(int year) {
        return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
    }

    private static int daysInMonth(int month, boolean leap) {
        if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            return 31;
        } else if (month == 2) {
            if (leap) {
                return 29;
            } else {
                return 28;
            }
        } else {
            return 30;
        }
    }
}