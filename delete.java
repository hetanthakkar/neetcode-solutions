import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.fail;

import org.junit.Test;

import java.util.Random;

public abstract class AbstractQuestionTest {

    protected final String longRandom;
    protected String[] answers;
    protected String[] inCorrectAnswers;

    public AbstractQuestionTest() {
        longRandom = "aosdifjaso oifhas;ldihv;al skdfha;osidghv;osiadhvbasdjkhvn";
    }

    protected abstract Question createValidQuestion(String text);

    @Test
    public void testCreateValidQuestion() {
        Random r = new Random(200);
        for (int i = 0; i < 1000; i++) {
            int start = r.nextInt(longRandom.length() - 1);
            int end = start + r.nextInt(longRandom.length() - start - 1) + 1;
            String questionText = longRandom.substring(start, end);
            Question q = createValidQuestion(questionText + "?");

            assertEquals(questionText + "?", q.getQuestionText());
        }
    }

    @Test(expected = IllegalArgumentException.class)
    public void testCreateQuestionNoText() {
        createValidQuestion("");
    }

    @Test
    public void testAnswerCorrectly() {

        for (String answer : this.answers) {
            Question q = createValidQuestion("Is this a trick question?");
            assertFalse(q.hasBeenAnswered());

            q.answer(answer);
            assertEquals(answer.toLowerCase(), q.getEnteredAnswer());
            assertTrue(q.hasBeenAnswered());
        }
    }

    @Test
    public void testAnswerInCorrectly() {
        for (String answer : this.inCorrectAnswers) {
            Question q = createValidQuestion("Is this a trick question?");
            assertFalse(q.hasBeenAnswered());

            try {
                q.answer(answer);
                fail("Likert question accepted an invalid answer");
            } catch (IllegalArgumentException e) {
                assertFalse(q.hasBeenAnswered());
            }
        }
    }
}
