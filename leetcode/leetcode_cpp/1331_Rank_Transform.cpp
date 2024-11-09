/*
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

    Rank is an integer starting from 1.
    The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
    Rank should be as small as possible.
*/

#include<iostream>
#include<vector>
#include<bits/stdc++.h>
#include<unordered_map>
using namespace std;

vector<int> solutionRank(vector<int> &arr){
    vector<int> cpy(arr.begin(), arr.end());
    vector<int> sol(arr.begin(), arr.end());
    unordered_map<int,int> rankMap;
    sort(cpy.begin(), cpy.end());
    //remove duplicates
    cpy.erase( unique(cpy.begin(), cpy.end()), cpy.end() );
    for(int i=0;i<cpy.size();i++){
        rankMap[cpy[i]] = i+1;
    }
    for(int i=0;i<arr.size();i++){
        sol[i] = rankMap[arr[i]];    
    }
    return sol;
}

int main(){
    vector<int> arr = {40,20,30,10,40,50,10};
    vector<int> sol = solutionRank(arr);

    for(int i=0;i<arr.size();i++)
        cout<<sol[i];
    return 0;
}