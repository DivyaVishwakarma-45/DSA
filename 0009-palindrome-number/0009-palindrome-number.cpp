class Solution {
public:

    bool isPalindrome(int x) {
        int copyNum = x;
        int revNum = 0;
        if(x<0){
            return false;
        }
        while(x != 0){
            int rem = x%10;
            if(revNum > INT_MAX/10 || revNum < INT_MIN/10){
                return false;
            }
            revNum = revNum*10+rem;
            x=x/10;
        }
        return copyNum == revNum;
    }
};