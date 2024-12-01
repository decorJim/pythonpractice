

public class Main {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {}

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public static TreeNode searchBST(TreeNode root, int val) {
        if (root == null) {
            return null;
        }

        if (root.val == val) {
            return root;
        }

        if (root.val < val) {
            return searchBST(root.right, val);
        }
        else {
            return searchBST(root.left, val);
        }
    }


    public static void main(String[] args) {

        TreeNode l3_n1 = new TreeNode(1, null, null);
        TreeNode l3_n3 = new TreeNode(3, null, null);

        TreeNode l2_n2 = new TreeNode(2, l3_n1, l3_n3);
        TreeNode l2_n7 = new TreeNode(7, null, null);

        TreeNode l1_n4 = new TreeNode(4, l2_n2, l2_n7);

        System.out.println(searchBST(l1_n4, 2).val);
        System.out.println(searchBST(l1_n4, 5));

    }
}