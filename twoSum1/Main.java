import java.util.Arrays;
import java.util.HashMap;

public class Main {

    public static int[] twoSum(int[] nums, int target) {

        HashMap<Integer, Integer> complements = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (complements.containsKey(complement)) {
                int num = complements.get(complement);
                return new int[] { i, num };
            }
            complements.put(nums[i], i);
        }

        int[] ans = {};
        return ans;
    }

    public static void main(String[] args) {

        int [] nums = {2,3,6,3,6};
        int target = 5;
        System.out.println(Arrays.toString(twoSum(nums, target)));

        int [] nums2 = {-3,-2,0,3,4,6,5,-8};
        target = -5;
        System.out.println(Arrays.toString(twoSum(nums2, target)));

        int [] nums3 = {3,2,4};
        target = 6;
        System.out.println(Arrays.toString(twoSum(nums3, target)));

    }
}