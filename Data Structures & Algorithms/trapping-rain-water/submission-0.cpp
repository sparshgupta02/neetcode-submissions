class Solution {
public:
    int trap(vector<int>& height) {
        int curr=height[0];
        int n=height.size();
        int res=0;
        vector<int> maxleft(n,0);
        vector<int> maxright(n,0);
        vector<int> miner(n,0);
        for(int i=1;i<n;i++){
            maxleft[i]=curr;
            curr=max(curr,height[i]);
        }
        curr=height[n-1];
        for(int i=n-2;i>=0;i--){
            maxright[i]=curr;
            curr=max(curr,height[i]);
        }
        for(int i=0;i<n;i++){
            miner[i]=min(maxleft[i],maxright[i]);
            res+=max(0,miner[i]-height[i]);
        }
        return res;        
    }
};
