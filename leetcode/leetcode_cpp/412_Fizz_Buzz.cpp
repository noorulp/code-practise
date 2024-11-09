#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
    
    int n = 15,i = 0;
    vector<string> ans(n);
    
    for(int i=1;i<=n;i++){
        
        if( i%15 == 0){
            ans[i-1]="fizzbuzz";
        }
        else if( i%3 == 0){
            ans[i-1]="fizz";
        }
        else if( i%5 == 0){
            ans[i-1]="buzz";
        }
        else{
            ans[i-1]=i + "";
        }
    }

    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<",";
    }

    return 0;
}