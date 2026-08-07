class Solution {
    vector<int> dp;
public:
    int f(int n,vector<int>& cost){
        if(dp[n]!=-1) return dp[n];
        int l=f(n-1,cost);
        int r=f(n-2,cost);
        return dp[n] = min(l+cost[n-1],r+cost[n-2]);

    }
    int minCostClimbingStairs(vector<int>& cost) {
        int n=cost.size();
        dp=vector<int>(n+1,-1);
        dp[0]=0;dp[1]=0;
        return f(n,cost);


        
    }
};
