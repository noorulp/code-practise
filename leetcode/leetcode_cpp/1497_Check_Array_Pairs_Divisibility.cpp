/*Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is divisible by k.

Return true If you can find a way to do that or false otherwise.*/

#include<iostream>
#include<vector>
using namespace std;

int main(){

    vector<int> arr{ -1,1,-2,2,-3,3,-4,4 };
    int k=3, l = arr.size();

    vector<int> diffArray(k,0);
    for(int i=0;i<l;i++){
        int diff = arr[i]%k; 
        if( diff <0 )
            diffArray[k + diff]++;
        else
            diffArray[diff]++;
    }

    if(diffArray[0]%2 != 0){
        cout<<false;
    }
    if(k %2 == 0){
        for(int i=1;i<k/2;i++){
            if ( diffArray[i] != diffArray[k-i] )
                cout<<false;
        }
        if( diffArray[k/2]%2 == 1)
            cout<<false;
    }
    else{
        for(int i=1;i<=k/2;i++){
            if ( diffArray[i] != diffArray[k-i] )
                cout<<false;
        }
    }
    cout<<true;
    return 0;
}