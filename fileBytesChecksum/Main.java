import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main {

    public static List<Integer> checkSum(int[] fileBytes) {
        Stack<Integer> s=new Stack<>();
        /**
         *  [3,265,132,10,2,165,6]
             s  i       - s  j  -
         *   count=fileBytes[i]
         *   j=i+1
         *   size=fileBytes[i]
         *
         */

        int start=0;
        List<Integer> checksums=new ArrayList<>();
        while(start<fileBytes.length) {
            int size=fileBytes[start];
            int i=start+1; /** position after is content */
            int count=0;
            int sum=0;
            while(count<size) {
                sum+=fileBytes[i];
                i++;
                count++;
            }
            checksums.add(sum);
            start=start+size+1;
        }
        for(int sum:checksums) {
            System.out.println(sum);
        }
        return checksums;
    }

    public static void main(String[] args) {
       int[] fileBytes={3,265,132,2,2,165,6};
       checkSum(fileBytes);
    }
}