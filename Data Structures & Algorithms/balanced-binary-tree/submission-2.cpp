/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root==NULL) return 0;
        return 1+max(maxDepth(root->left),maxDepth(root->right));        
    }
    vector<int> dfs(TreeNode* root){
        if(root==NULL) return {1,0};
        vector<int> left=dfs(root->left);
        vector<int> right=dfs(root->right);
        bool bal =(left[0] == 1 && right[0] == 1) && 
                        (abs(left[1] - right[1]) <= 1);
        int height = 1+max(left[1],right[1]);
        return {bal?1:0,height};

    }
    bool isBalanced(TreeNode* root) {
        return dfs(root)[0]==1;
        
    }
};
