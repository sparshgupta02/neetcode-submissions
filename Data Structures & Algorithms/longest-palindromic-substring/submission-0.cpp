class Solution {
public:
    string longestPalindrome(string s) {
        int reslen=1;
        int res=0;
        int n=s.size();
        //checking odd len
        for(int i=0;i<n;i++){
            int temp=1;
            int j=1;
            while(i-j>=0 && i+j<n){
                if(s[i+j]==s[i-j]){
                    temp+=2;
                    j++;
                }
                else break;
            }
            if(temp>reslen){
                res=i-j+1;
                reslen=temp;
            }
        }
        for(int i=0;i<n-1;i++){
            if(s[i]==s[i+1]){
                int temp=2;
                int j=1;
                while(i-j>=0 && i+j+1<n){
                    if(s[i-j]==s[i+j+1]){
                        temp+=2;
                        j++;
                    }
                    else break;
                }
                if(temp>reslen){
                res=i-j+1;
                reslen=temp;
            }          

            }
        }
        return s.substr(res, reslen);

        
    }
};
