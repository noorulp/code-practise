#include<iostream>
#include<vector>

using namespace std;

vector<int> spiralOrder2(vector<vector<int>>& matrix){
    int m=matrix.size(),n=matrix[0].size();
    vector<int> spiral(m*n,0);
    int dir=0,i=0,j=-1, offset=0; //0-toprow, 1-rightrow, 2-bottomrow, 3-leftrow
    for(int k=0; k<spiral.size();k++){
        if(dir==0){ //top
            j++;
            if( j==n-offset-1 )
                dir=1;
            else if( j>n-offset-1 ){
                j--;
                dir=1;
                i++;
            }
        }
        else if(dir==1){ //right
            i++;
            if( i==m-offset-1 )
                dir=2;
        }
        else if(dir==2){ //bottom
            j--;
            if( j==offset )
                dir=3;
        }
        else{  //left
            i--;
            if( i==offset ){
                dir=0;
                offset++;
                i=offset;
                j=offset;
            }
        }
        spiral[k]=matrix[i][j];
    }
    return spiral;

}

vector<int> spiralOrder( vector<vector<int>>& matrix){
    int index=0,m=matrix.size(),n=matrix[0].size();
    vector<int> spiral(m*n,0);
    int limit=(m<n)?m:n;
    //FULL SPIRALS  
    for(int offset=0;offset<limit/2;offset++){
        int j=offset, i=offset;
        //top
        while(j<n-offset-1){
            spiral[index++]=matrix[i][j++];
        }
        //left
        while(i<m-offset-1){
            spiral[index++]=matrix[i++][j];
        }
        //bottom
        while(j>offset){
            spiral[index++]=matrix[i][j--];
        }
        //right
        while(i>offset){
            spiral[index++]=matrix[i--][j];
        }
    }
    if(limit%2==1){
        int offset=limit/2;
        int i=offset,j=offset;
        if(m<n){
            //top array
            while(j<n-offset){
                spiral[index++]=matrix[i][j++];
            }
        }
        else{
            //right array
            while(i<m-offset){
                spiral[index++]=matrix[i++][j];
            }
        }
    }

    return spiral;
}

int main(){
    vector<vector<int>> matrix = { {1,2,3}, {4,5,6},{7,8,9}, {10,11,12} };
    //matrix={ {1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16},{17,18,19,20},{21,22,23,24} };   
    //matrix{ {1},{2}};  //matrix={ {1,2,3,4} ,{5,6,7,8}, {9,10,11,12} };    
    vector<int> sol=spiralOrder(matrix);
    return 0;
}