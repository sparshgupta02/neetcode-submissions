class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> a;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(a.count(nums[i])){
                return true;
            }
            else {
                a.insert(nums[i]);
            }
        
                
        }
        return false;
    }
};