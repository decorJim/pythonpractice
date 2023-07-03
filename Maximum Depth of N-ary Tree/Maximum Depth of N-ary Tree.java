/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public int maxDepth(Node root) {
        int maxDept=0;
        return dfs(root,maxDept);
    }
    
    public int dfs(Node n, int dept) {
        if(n==null) return 0;  // once reaching a node who has no childrens it goes back to the previous dfs call
            
        int max = 0;
        // for every children of the nodes call function again with recursion 
        // if I have 3 children node I set the new max to the node who has the most descendents
        for(Node child: n.children) {
            // for example my childrens are node 5 and node 6
            // maxDepth call for node 5 return value is return value of dfs is 1
            // maxDepth call for node 6 return value is return value of dfs is 1
            max = Math.max(max, maxDepth(child));
        }
        // starting off the bottom of the tree every time a node goes back to
        // its parent, increase depth by 1 
        return 1 + max;
    }
    
}