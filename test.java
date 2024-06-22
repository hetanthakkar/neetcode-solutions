package vehicle;

public class RegularManualTransmission implements ManualTransmission {

    private int speed;
    private int gear;
    private int statusIndex;
    private static int[] gearRanges;
    private final String[] statusMessages;
    int[] lowerRanges;
    int[] higherRanges;

    public RegularManualTransmission(int l1, int h1, int l2, int h2, int l3, int h3, int l4, int h4,
            int l5, int h5) {

        if (!(l1 <= h1 && l2 <= h2 && l3 <= h3 && l4 <= h4 && l5 <= h5)) {
            throw new IllegalArgumentException("lx should be less that equal to hx");
        }

        if (!(l1 < l2 && l2 < l3 && l3 < l4 && l4 < l5)) {
            throw new IllegalArgumentException(
                    "the lower speed for gear x should be strictly lesser than lower speed of gear x+1");
        }

        if (l2 - h1 > 0 || l3 - h2 > 0 || l4 - h3 > 0 || l5 - h4 > 0) {
            throw new IllegalArgumentException(
                    "adjacent-gear ranges may overlap but the ranges cannot be non-overlapping");
        }

        if (l1 != 0) {
            throw new IllegalArgumentException("l1 should be 0");
        }

        gearRanges = new int[] { l1, h1, l2, h2, l3, h3, l4, h4, l5, h5 };
        statusMessages = new String[] {
                "OK: everything is OK.",
                "OK: you may increase the gear.",
                "OK: you may decrease the gear.",
                "Cannot increase speed, increase gear first.",
                "Cannot decrease speed, decrease gear first.",
                "Cannot increase gear, increase speed first.",
                "Cannot decrease gear, decrease speed first.",
                "Cannot increase speed. Reached maximum speed.",
                "Cannot decrease speed. Reached minimum speed.",
                "Cannot increase gear. Reached maximum gear.",
                "Cannot decrease gear. Reached minimum gear."
        };

        // Initialize the object in the first gear with zero speed
        speed = 0;
        gear = 1;
        statusIndex = 0;
        lowerRanges = new int[] { l1, l2, l3, l4, l5 };
        higherRanges = new int[] { h1, h2, h3, h4, h5 };
    }

    @Override
    public String getStatus() {
        return statusMessages[statusIndex];
    }

    @Override
    public int getSpeed() {
        return speed;
    }

    @Override
    public int getGear() {
        return gear;
    }

    @Override
    public ManualTransmission increaseSpeed() {
        int newSpeed = speed + 1;

        // "Cannot increase speed. Reached maximum speed.",

        if (newSpeed > higherRanges[4]) {
            statusIndex = 7;
            return this;
        }
        // "Cannot increase speed, increase gear first.",
        if (newSpeed > higherRanges[gear - 1]) {
            statusIndex = 3;
            return this;
        }

        // "OK: you may increase the gear.",
        if (gear < 5 && newSpeed >= lowerRanges[gear]) {
            speed = newSpeed;
            statusIndex = 1;
            return this;
        }

        // "OK: everything is OK.",
        speed = newSpeed;
        statusIndex = 0;
        return this;
    }

    @Override
    public ManualTransmission decreaseSpeed() {
        int newSpeed = speed - 1;

        // "Cannot decrease speed. Reached minimum speed.",
        if (newSpeed < lowerRanges[0]) {
            statusIndex = 8;
            return this;
        }

        // "Cannot decrease speed, decrease gear first.",
        if (newSpeed < lowerRanges[gear - 1]) {
            statusIndex = 4;
            return this;
        }

        // "OK: you may decrease the gear.", // 2
        if (gear >= 2 && newSpeed >= lowerRanges[gear - 1] && newSpeed <= higherRanges[gear - 2]) {
            statusIndex = 2;
            speed = newSpeed;
            return this;
        }

        speed = newSpeed;
        statusIndex = 0;
        return this;

    }

    @Override
    public ManualTransmission increaseGear() {

        // "Cannot increase gear. Reached maximum gear.",
        int newGear = gear + 1;
        if (newGear > 5) {
            statusIndex = 9;
            return this;
        }

        // "Cannot increase gear, increase speed first.",
        if (lowerRanges[gear] > speed) {
            statusIndex = 5;
            return this;
        }

        // "OK: everything is OK.",
        gear = newGear;
        statusIndex = 0;
        return this;

    }

    @Override
    public ManualTransmission decreaseGear() {
        int newGear = gear - 1;

        // "Cannot decrease gear. Reached minimum gear."
        if (newGear <= 0) {
            statusIndex = 10;
            return this;
        }

        // "Cannot decrease gear, decrease speed first."
        if (speed > higherRanges[gear - 2]) {
            statusIndex = 6;
            return this;
        }

        // "OK: everything is OK."
        gear = newGear;
        statusIndex = 0;
        return this;

    }

}
