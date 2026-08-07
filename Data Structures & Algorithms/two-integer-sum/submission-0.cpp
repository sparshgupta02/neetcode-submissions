class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n=nums.size();
        map<int,int> a;
        for(int i=0;i<n;i++){
            a[nums[i]]=i;
        }
        for (int i=0;i<n;i++){
            int diff = target-nums[i];
            if(a.count(diff)&& a[diff]!=i){
                return {i,a[diff]};
            }
        }
        return {};
        
    }
};
