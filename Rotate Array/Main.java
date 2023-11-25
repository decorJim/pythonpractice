import java.util.*;
import java.util.concurrent.atomic.AtomicIntegerArray;

public class Main {

    public static int[] rotateArray(int[] nums,int k) {

        Arrays.stream(nums).forEach(num->{
            System.out.print(num+" ");
        });
        System.out.println();


        /** reverse the whole array */
       int i=0;
       int j=nums.length-1;

       while(i<j) {
           int temp=nums[i];
           nums[i]=nums[j];
           nums[j]=temp;
           i++;
           j--;
       }


       Arrays.stream(nums).forEach(num->{
           System.out.print(num+" ");
       });
        System.out.println();

        /** reverse the first k elements */
        i=0;
        j=k-1;
        while(i<j) {
            int temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
            i++;
            j--;
        }

        /** reverse the rest of elements */
        i=k;
        j=nums.length-1;
        while(i<j) {
            int temp=nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
            i++;
            j--;
        }

        Arrays.stream(nums).forEach(num->{
            System.out.print(num+" ");
        });

        return nums;
    }

    public static void main(String[] args) {
       int nums[]={3,4,2,5,6,8};

       rotateArray(nums,2);

    }
}