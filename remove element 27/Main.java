import java.util.Arrays;

public class Main {

    public static int removeElement(int[] nums,int val) {

        System.out.println("original");
        for(int num:nums) {
            System.out.print(num+" ");
        }
        System.out.println();

        /** pointer to detect element to remove */
        int i=0;
        /** pointer to find the replacement */
        int j=0;

        while(i<nums.length) {

            /** only move if it is not val */
            if(nums[i]!=val) {
                nums[j]=nums[i];
                j++;
            }
            /** if value found j will keep track of it */

            /** i will replace val by replacement */
            i++;

        }

        System.out.println("after remove val: "+val);
        for(int num:nums) {
            System.out.print(num+" ");
        }
        System.out.println();


        return j;
    }

    public static void main(String[] args) {
        /**
         *  [2,3,4,5,2,3,5]   remove 2
         *  ji
         *  [2,3,4,5,2,3,5]
         *   i j
         *  [2,3,4,5,2,3,5]
         *   i j
         *  [3,3,4,5,2,3,5]
         *   i   j
         *  [2,3,4,5,2,3,5]
         *     i j
         *  [2,3,4,5,2,3,5]
         */

        int[] nums={2,3,4,5,2,3,5};
        System.out.println(removeElement(nums,2));

        int[] nums2={4,6,8,4,7,9,5};
        System.out.println(removeElement(nums2,8));

    }
}