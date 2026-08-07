class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int> a,b;
        int n=s.size();
        int m=t.size();
        if (n !=m) return false;
        for (int i=0;i<n;i++){
            a[s[i]]++;
            b[t[i]]++;
        }
        return a==b;
        
    }
};
