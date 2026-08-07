class Solution {
private:
    vector<int> dp;
public:
    int f(int n){
        if(dp[n]!=-1) return dp[n];
        return dp[n]=f(n-1)+f(n-2);
    }
    int climbStairs(int n) {
        dp = vector<int>(n+1,-1);
        dp[0]=1;dp[1]=1;
        return f(n);        
    }
};
