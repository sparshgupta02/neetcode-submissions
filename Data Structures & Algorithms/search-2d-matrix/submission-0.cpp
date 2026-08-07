class Solution {
public:
    bool search(vector<int>& nums, int target) {
            int l = 0, r = nums.size() - 1;

            while (l <= r) {
                int m = l + ((r - l) / 2);
                if (nums[m] > target) {
                    r = m - 1;
                } else if (nums[m] < target) {
                    l = m + 1;
                } else {
                    return true;
                }
            }
            return false;
        }
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        vector<int> nums;
        int m=matrix.size();
        int n=matrix[0].size();
        for(int i=0;i<m;i++){
            nums.insert(nums.end(), matrix[i].begin(), matrix[i].end());
        }
        return search(nums,target);
    }
};
