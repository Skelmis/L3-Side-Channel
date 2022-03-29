import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

public class LoopTime {
    public static void main(String[] args){
        // 4 bytes per int
        // 256 is 1kb for ints
        LoopTime listTime = new LoopTime();
        ArrayList<Long> timings = new ArrayList<Long>();


        double base = 0.5;
        double val = 0;
        for (int i = 1; i < 17; i++) {
            int arrSize = listTime.getArraySizeFor(base * i + val);
            System.out.println(base * i + val);
            timings.add(listTime.runLoop(arrSize));
        }

        try {
            FileWriter myWriter = new FileWriter("loop_lookups.txt");
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

    public long runLoop(int size){
        int[] arr = new int[size];

        // Try clean cache??
        System.gc();

        // Every 16 is a new cache line
        long start = System.nanoTime();
        for (int i = 0; i < size; i += 1) {
            arr[(i * 16) % (size-1)]++;
        }
        return System.nanoTime() - start;
    }

    /**
     *
     * @param requestedSize How big in mb we want the array to be
     * @return int The required array size
     */
    public int getArraySizeFor(double requestedSize) {
        // Total items required for 1 mb
        int intByteToMb = 1000000 / 4;
        return (int) (intByteToMb * requestedSize);
    }
}
