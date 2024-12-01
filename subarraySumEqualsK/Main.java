import java.util.*;

public class Main {

    public static int subarraySumEqualsK(int[] nums, int k) {

        /** prefix, count */
        HashMap<Integer, Integer> prefixes = new HashMap<>() {{ put(0,1); }};
        int currentSum = 0;

        int countSubarrays = 0;

        for (int num:nums) {
            currentSum += num;

            int prefix = currentSum - k;

            if (prefixes.containsKey(prefix)) {
                countSubarrays += prefixes.get(prefix);
            }

            if (prefixes.containsKey(currentSum)) {
                int count =  prefixes.get(currentSum);
                count += 1;
                prefixes.put(currentSum, count);
            }
            else {
                prefixes.put(currentSum, 1);
            }

        }

        return countSubarrays;


    }

    public static void main(String[] args) {

        int[] nums = {1,1,1};
        int target = 2;

        System.out.println(subarraySumEqualsK(nums, target));

        nums = new int[] {1,2,3};
        target = 3;

        System.out.println(subarraySumEqualsK(nums, target));

        nums = new int[] {1,2,1,2,1};
        target = 3;

        System.out.println(subarraySumEqualsK(nums, target));
    }
}