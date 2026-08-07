class Solution {
public:
    int countSubstrings(string s) {
        int res=0;
        int n=s.size();
        for(int i=0;i<n;i++){
            int j=1;
            res++;
            while(i-j>=0 && i+j<n){
                if(s[i+j]==s[i-j]){;
                    j++;
                    res++;
                }
                else break;
            }
        }
        for(int i=0;i<n-1;i++){
            if(s[i]==s[i+1]){
                res++;
                int j=1;
                while(i-j>=0 && i+j+1<n){
                    if(s[i-j]==s[i+j+1]){
                        res++;
                        j++;
                    }
                    else break;
                }        

            }
        }
        return res;       
        
    }
};
