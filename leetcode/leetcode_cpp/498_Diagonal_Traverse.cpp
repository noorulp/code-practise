#include<iostream>
#include<vector>
using namespace std;

vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
    //int i=0,j=0, dir=-1; //updwards=-1, downwards=1
    int m=mat.size(), n=mat[0].size();
    int index=1;
    vector<int> diagonal(m*n,0);
    diagonal[0]=mat[0][0];
    for(int k=1;k<m+n-1;k++){
        int i,j;
        if(k%2==1){
            //find toprightmost element
            j=(k<n)?k:n-1;
            i=k-j;
            while(i<m && j>=0){
                diagonal[index++]=mat[i][j];
                i++;
                j--;
            }
        }
        else{
            //find bottomleftmost element
            i=(k<m)?k:m-1;
            j=k-i;
            while(i>=0 && j<n){
                diagonal[index++]=mat[i][j];
                i--;
                j++;
            }
        }
    }

    return diagonal;
}

int main(){
    vector<vector<int>> matrix={ {1,2},{3,4}, {5,6},{7,8} };
    vector<int> diag=findDiagonalOrder(matrix);
    return 0;
}