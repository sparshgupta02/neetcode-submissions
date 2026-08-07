class Solution {
public:
int nCr(int n, int r){
    
    double sum = 1;

    // Calculate the value of n choose
    // r using the binomial coefficient formula
    for (int i = 1; i <= r; i++){
        
        sum = sum * (n - r + i) / i;
    }
    return (int)sum;
}
    int uniquePaths(int m, int n) {
        int k=m+n-2;
        int r=n-1;
        return nCr(k,r);
        
    }
};
