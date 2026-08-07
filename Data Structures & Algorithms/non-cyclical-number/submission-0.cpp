class Solution {
public:
    int sum(int n){
        int res=0;
        string s =to_string(n);
        for(char c:s){
            res += (c - '0') * (c - '0');
        }
        return res;
    }
    bool isHappy(int n) {
        set<int> visit;
        while(visit.find(n)==visit.end()){
            visit.insert(n);
            n=sum(n);
            if(n==1){
                return true;
            }
        }
        return false;

    }
};
