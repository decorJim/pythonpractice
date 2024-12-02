public class Main {

    public static int removeDuplicatesFromSortedArray(int[] nums) {

        if (nums.length == 1) {
            return 0;
        }

        int marker = 1;

        for (int i = 0; i < nums.length; i++) {
            if(i - 1 >= 0 && nums[i] != nums[i-1]) {
                nums[marker] = nums[i];
                marker++;
            }
        }

        return marker;
    }

    public static void main(String[] args) {

        System.out.println(removeDuplicatesFromSortedArray(new int[] {1,1,2}));
        
    }
}