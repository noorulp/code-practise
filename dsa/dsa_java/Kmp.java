package dsa_java;

class Kmp{

    static int[] lps(String pattern){
        int M=pattern.length();
        int[] arr= new int[M];
        int len=0,i=1;
        arr[0]=0;
        while(i<M){
            if( pattern.charAt(i)==pattern.charAt(len) ){
                len++;
                arr[i]=len;
                i++;
            }
            else{
                if( len!=0 ){
                    len=arr[len-1];
                }
                else{
                    arr[i]=0;
                    i++;
                }
            }
        }
        return arr;
    }
    //Kmp algorithm
    static int stringSearch(String str, String pattern){
        int i=0, j=0, sol=0, M=str.length(), N=pattern.length();
        int[] prefixArray = lps(pattern);
        
        while( i<M ){
            if( str.charAt(i)==pattern.charAt(j) ){
                i++;
                j++;
            }
            if( j==N ){
                j=prefixArray[j-1];
                sol++;
            }
            else if( i<M && str.charAt(i)!=pattern.charAt(j) ){
                if( j==0 ){
                    i++;
                }
                else{
                    j=prefixArray[j-1];
                }
            }
        }
        
        return sol;
    }

    public static void main(String[] args){
        String str = "aabacaaabaabaa", pattern="aabaa";
        //int[] prefix=lps("aaacaaaaac");
        //System.out.println(prefix[0]);
        System.out.println(stringSearch(str, pattern));
    }
}