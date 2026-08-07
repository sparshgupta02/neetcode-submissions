class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.empty()) return 0;
        int l=0;int res=1;int r=1;
        set<char> a;
        a.insert(s[0]);
        while(r<s.size()){
            if(a.count(s[r])){
                res=max(res,r-l);
                a.erase(s[l]);
                l++;
            }
            else{
                a.insert(s[r]);
                r++;
                res=max(res,r-l);

            }
        }
        return res;
        
    }
};
