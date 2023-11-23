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

        while(j<nums.length) {

            /** only move if it is not val */
            if(nums[i]!=val) {
                i++;
            }
            /** if value found i will keep track of it */

            /** j will replace val by replacement */
            nums[i]=nums[j];
            j++;

        }

        System.out.println("after remove val: "+val);
        for(int num:nums) {
            System.out.print(num+" ");
        }

        return 1;
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
        removeElement(nums,2);

    }
}