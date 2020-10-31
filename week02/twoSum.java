import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class twoSum {
    public static void main(String[] args) {
        int[] result = new int[2];
        int[] nums=new int[] { 2, 7, 11, 12};
        int target = 9;
        result = twoSum( nums, target);
        System.out.println(Arrays.toString(result));

    }

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashtable = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (hashtable.containsKey(target - nums[i])) {
                System.out.println(i);
                return  new int[]{hashtable.get(target - nums[i]), i};
            }
            hashtable.put(nums[i], i);
        }
        return new int[0];
    }

}
