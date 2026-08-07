class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        map<char,char> m={{')','('},{']','['},{'}','{'}};
    for(char c:s){
        if(m.count(c)){
            if(!stack.empty() && stack.top()==m[c]){
                stack.pop();
            }
            else return false;
        }
        else{
            stack.push(c);
        }
    }
    return stack.empty();
    }
};
