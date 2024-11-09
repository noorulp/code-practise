/*Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.*/
#include<iostream>
using namespace std;

int main(){

    int num=123, ans=0;
    int e=1, count=-1;
    while(e<=num){
        if (num&e)
            count++;
        
        e=e*2;
        count++;
    }

    if(count == -1)
        ans = 0;
    else
        ans = count;

    return 0;
}