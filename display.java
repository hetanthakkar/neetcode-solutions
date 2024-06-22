import static org.junit.Assert.assertEquals;
import org.junit.Before;
import org.junit.Test;
import vehicle.RegularManualTransmission;

/**
 * Test cases for the RegularManualTransmission class.
 */
public class RegularManualTransmissionTest {

    // Test Cases for Speed Variable
    private static RegularManualTransmission transmission;

    @Before
    public void beforeFunction() {
        transmission = new RegularManualTransmission(0, 10, 8, 15, 15, 40, 40,
                60, 50, 100);
    }

    /**
     * Test for increasing the speed.
     */
    @Test
    public void testIncreaseSpeed() {
        // Setup
        assertEquals(1, transmission.increaseSpeed().getSpeed());
    }

    /**
     * Test for checking if Hi is greater than Hi+1 in the constructor.
     */
    @Test(expected = IllegalArgumentException.class)
    public void testHiGreaterThanHiPlusOne() {
        new RegularManualTransmission(0, 10, 8, 20, 9, 15, 15, 20, 20, 30);
    }

    /**
     * Test for decreasing the speed.
     */
    @Test
    public void testDecreaseSpeed() {
        // Setup
        assertEquals(0, transmission.decreaseSpeed().getSpeed());
    }

    /**
     * Test for increasing the speed within the same gear.
     */
    @Test
    public void testIncreaseSpeedSameGear() {
        // Setup
        transmission.increaseSpeed();
        assertEquals(2, transmission.increaseSpeed().getSpeed());
        assertEquals(1, transmission.increaseSpeed().getGear());
    }

    /**
     * Test for decreasing the speed within the same gear.
     */
    @Test
    public void testDecreaseSpeedSameGear() {
        // Setup
        transmission.increaseSpeed();
        assertEquals(0, transmission.decreaseSpeed().getSpeed());
        assertEquals(1, transmission.decreaseSpeed().getGear());
    }

    /**
     * Helper method to simulate a series of speed increases.
     */
    private static void setupIncrease() {
        for (int i = 0; i <= 10; i++) {
            transmission.increaseSpeed();
        }
        transmission.increaseGear();

        for (int i = 0; i <= 15; i++) {
            transmission.increaseSpeed();
        }

        transmission.increaseGear();

        for (int i = 0; i <= 30; i++) {
            transmission.increaseSpeed();
        }
        transmission.increaseGear();

        for (int i = 0; i <= 10; i++) {
            transmission.increaseSpeed();
        }
        transmission.increaseGear();

        for (int i = 0; i <= 80; i++) {
            transmission.increaseSpeed();
        }
        transmission.increaseGear();

        for (int i = 0; i <= 190; i++) {
            transmission.increaseSpeed();
        }
    }

    /**
     * Test for ensuring speed does not exceed the maximum.
     */
    @Test
    public void testSpeedNotExceedMaximum() {
        setupIncrease();
        assertEquals(100, transmission.getSpeed());
        assertEquals("Cannot increase speed. Reached maximum speed.", transmission.getStatus());
    }

    /**
     * Test for ensuring speed does not decrease below the minimum.
     */
    @Test
    public void testSpeedNotDecreaseMinimum() {
        transmission.decreaseSpeed();
        assertEquals(0, transmission.decreaseSpeed().getSpeed());
    }

    // Test Cases for Gear Variable

    /**
     * Test for increasing the gear.
     */
    @Test
    public void testIncreaseGear() {
        // Setup
        for (int i = 0; i <= 10; i++) {
            transmission.increaseSpeed();
        }
        transmission.increaseGear();

        assertEquals(2, transmission.increaseGear().getGear());
    }

    /**
     * Test for decreasing the gear.
     */
    @Test
    public void testDecreaseGear() {
        // Setup
        transmission.increaseGear();
        assertEquals(1, transmission.decreaseGear().getGear());
    }

    /**
     * Test for increasing the gear within the same speed.
     */
    @Test
    public void testIncreaseGearSameSpeed() {
        // Setup
        for (int i = 0; i <= 10; i++) {
            transmission.increaseSpeed();
        }
        transmission.increaseGear();

        assertEquals(2, transmission.increaseGear().getGear());
        assertEquals(10, transmission.getSpeed());
    }

    /**
     * Test for decreasing the gear within the same speed.
     */
    @Test
    public void testDecreaseGearSameSpeed() {
        // Setup
        transmission.increaseGear();
        assertEquals(1, transmission.decreaseGear().getGear());
        assertEquals(0, transmission.getSpeed());
    }

    /**
     * Test for ensuring gear does not exceed the maximum.
     */
    @Test
    public void testGearNotExceedMaximum() {
        setupIncrease();
        transmission.increaseGear();
        assertEquals(5, transmission.getGear());
        assertEquals("Cannot increase gear. Reached maximum gear.", transmission.getStatus());
    }

    /**
     * Test for ensuring gear does not go below the minimum.
     */
    @Test
    public void testGearNotBeLessThanMin() {
        transmission.decreaseGear();
        assertEquals("Cannot decrease gear. Reached minimum gear.", transmission.getStatus());
    }

    /**
     * Test for ensuring speed does not go below the minimum.
     */
    @Test
    public void testSpeedNotBeLessThanMin() {
        transmission.decreaseSpeed();
        assertEquals("Cannot decrease speed. Reached minimum speed.", transmission.getStatus());
    }

    /**
     * Test for ensuring gear does not decrease below the minimum.
     */
    @Test
    public void testGearNotDecreaseMinimum() {
        transmission.decreaseGear();
        assertEquals(1, transmission.decreaseGear().getGear());
    }

    // Test Cases for Constructors and Exceptions

    /**
     * Test for L1 should be zero.
     */
    @Test(expected = IllegalArgumentException.class)
    public void testL1ShouldBeZero() {
        new RegularManualTransmission(1, 10, 8, 15, 15, 40, 40, 60, 50, 100);
    }

    /**
     * Test for L should be less than or equal to H.
     */
    @Test(expected = IllegalArgumentException.class)
    public void testLShouldBeLessThanOrEqualToH() {
        new RegularManualTransmission(0, 5, 5, 3, 11, 15, 16, 20, 21, 25);
    }

    /**
     * Test for Li less than Li+1.
     */
    @Test(expected = IllegalArgumentException.class)
    public void testLiLessThanLiPlusOne() {
        new RegularManualTransmission(0, 5, 5, 10, 4, 15, 16, 20, 21, 25);
    }

    /**
     * Test for adjacent gear ranges overlap.
     */
    @Test(expected = IllegalArgumentException.class)
    public void testAdjacentGearRangesOverlap() {
        new RegularManualTransmission(0, 5, 6, 10, 9, 15, 16, 20, 21, 25);
    }

    /**
     * Test for ensuring gear is positive.
     */
    @Test(expected = IllegalArgumentException.class)
    public void testGearPositive() {
        new RegularManualTransmission(-10, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    }

    /**
     * Test for initial status.
     */
    @Test
    public void initialStatus() {
        assertEquals("OK: everything is OK.", transmission.getStatus());
    }

    /**
     * Test for status when speed is changed.
     */
    @Test
    public void statusOkWhenSpeedChanged() {
        for (int i = 0; i < 5; i++) {
            transmission.increaseSpeed();
        }
        assertEquals("OK: everything is OK.", transmission.getStatus());
    }

    /**
     * Test for status when increasing speed to reach the range of the next gear.
     */
    @Test
    public void mayIncreaseGearStatus() {
        // Increase speed to reach the range of gear 2
        for (int i = 0; i < 9; i++) {
            transmission.increaseSpeed();
        }
        assertEquals("OK: you may increase the gear.", transmission.getStatus());
    }

    /**
     * Test for status when decreasing speed to reach the range of the previous
     * gear.
     */
    @Test
    public void mayDecreaseGearStatus() {
        // Increase speed to reach the range of gear 2
        for (int i = 0; i < 9; i++) {
            transmission.increaseSpeed();
        }
        transmission.increaseGear(); // Gear is now 2
        transmission.decreaseSpeed();
        assertEquals("OK: you may decrease the gear.", transmission.getStatus());
    }

    /**
     * Test for status when decreasing speed and gear range is high.
     */
    @Test
    public void speedDecreaseGearHigh() {
        // Increase speed to reach the range of gear 2
        for (int i = 0; i < 9; i++) {
            transmission.increaseSpeed();
        }
        transmission.increaseGear(); // Gear is now 2

        for (int i = 0; i < 10; i++) {
            transmission.decreaseSpeed();
        }
        assertEquals("Cannot decrease speed, decrease gear first.", transmission.getStatus());
    }

    /**
     * Test for status when increasing speed and gear range is low.
     */
    @Test
    public void speedIncreaseGearLow() {
        // Increase speed to reach the range of gear 2
        for (int i = 0; i < 912; i++) {
            transmission.increaseSpeed();
        }
        assertEquals("Cannot increase speed, increase gear first.", transmission.getStatus());
    }

    /**
     * Test for status when increasing gear and speed range is low.
     */
    @Test
    public void gearIncreaseSpeedLow() {
        transmission.increaseGear();
        assertEquals("Cannot increase gear, increase speed first.", transmission.getStatus());
    }

    /**
     * Test for status when decreasing gear and speed range is high.
     */
    @Test
    public void gearDecreaseSpeedHigh() {
        for (int i = 0; i < 10; i++) {
            transmission.increaseSpeed();
        }
        transmission.increaseGear();
        for (int i = 0; i < 5; i++) {
            transmission.increaseSpeed();
        }
        transmission.decreaseGear();
        assertEquals("Cannot decrease gear, decrease speed first.", transmission.getStatus());
    }
}
