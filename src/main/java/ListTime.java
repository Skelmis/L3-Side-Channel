import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class ListTime {
    public static void main(String[] args){
        // 4 bytes per int
        // 256 is 1kb for ints
        ListTime listTime = new ListTime();
        listTime.runLoop(listTime.getArraySizeFor(17));
    }

    public void runLoop(int size){I
        int[] arr = new int[size];
        ArrayList<Long> timings = new ArrayList<Long>();

        for (int i = 0; i < size; i++) {
            long start = System.nanoTime();
            int x = arr[i] + 1;
            long runtime = System.nanoTime() - start;
            timings.add(runtime);
        }
        System.out.println("Minimum Element in ArrayList = " + Collections.min(timings));
        System.out.println("Minimum Element in ArrayList = " + Collections.max(timings));

        try {
            FileWriter myWriter = new FileWriter("data.txt");
            for (long runtime : timings) {
                myWriter.write(Long.toString(runtime));
                myWriter.write("\n");
            }
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }

    /**
     *
     * @param requestedSize How big in mb we want the array to be
     * @return int The required array size
     */
    public int getArraySizeFor(int requestedSize) {
        // Total items required for 1 mb
        int intByteToMb = 1000000 / 4;
        return intByteToMb * requestedSize;
    }
}