import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;


public class Main {

    public static ArrayList<ArrayList<Integer>> treeSum(ArrayList<Integer> array,Integer target) {
        ArrayList<ArrayList<Integer>> results=new ArrayList<>();

        Collections.sort(array);
        System.out.println(array);

        for(int i=0;i<array.size();i++) {

            int k=i+1;
            int j=array.size()-1;

            while(k<j) {
                if(array.get(i)+array.get(k)+array.get(j)<target) {
                    k++;
                }
                if(array.get(i)+array.get(k)+array.get(j)>target) {
                    j--;
                }
                if(array.get(i)+array.get(k)+array.get(j)==target && i!=j && j!=k) {
                    ArrayList<Integer> sub_result=new ArrayList<>();
                    sub_result.addAll(
                            Arrays.asList(
                                    array.get(i),
                                    array.get(k),
                                    array.get(j)
                            )
                    );
                    results.add(sub_result);

                    k++;
                    while(array.get(k)==array.get(k-1) && k<j) {
                        k++;
                    }
                }

            }

        }
        return results;
    }

    public static void main(String[] args) {
        ArrayList<Integer> array=new ArrayList<Integer>(Arrays.asList(3,4,5,2,5,3,5));
        System.out.println(treeSum(array,15));
        System.out.println(treeSum(array,9));

        /**
         *   [3,4,5,2,5,3,5]    target=15
         *    i   k       j
         *   [2,3,3,4,5,5,5]
         */
    }
}