import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class Main {

    public static class TreeNode {
        final public Integer val;
        final public TreeNode left;
        final public TreeNode right;

        public TreeNode(Integer val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static List<List<Integer>> DFS(TreeNode root) {

        LinkedList<TreeNode> queue = new LinkedList<>() {{ add(root); }};
        List<List<Integer>> ans = new ArrayList<>();

        while (queue.isEmpty() == false) {

            ArrayList<Integer> currentLevel = new ArrayList<>();
            /** unlike python size is not saved so need to have variable save its value */
            int n = queue.size();

            for (int i=0; i < n; i++) {

                TreeNode node = queue.pollFirst();

                currentLevel.add(node.val);

                if(node.left != null) {
                    /** offer puts node to the back of list if add is used node is put to front of list */
                    queue.offer(node.left);
                }
                if(node.right != null) {
                    queue.offer(node.right);
                }
            }

            if (ans.size()%2 == 0) {
                Collections.reverse(currentLevel);
            }

            ans.add(currentLevel);

        }
        return ans;
    }

    public static void main(String[] args) {
        TreeNode l3_n15 = new TreeNode(15, null, null);
        TreeNode l3_n7 = new TreeNode(7, null, null);

        TreeNode l2_n9 = new TreeNode(9, null, null);
        TreeNode l2_n20 = new TreeNode(20, l3_n15, l3_n7);

        TreeNode l1_n3 = new TreeNode(3, l2_n9, l2_n20);

        System.out.println(DFS(l1_n3));

    }
}