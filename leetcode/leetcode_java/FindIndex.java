//28 KMP Java

class FindIndex {
    
    static int[] computeLps(String pattern){
        int[] arr = new int[pattern.length()];
        int len=0, i=1;
        arr[0]=0;
        while( i<pattern.length() ){
            if( pattern.charAt(i)==pattern.charAt(len) ){
                len++;
                arr[i]=len;
                i++;
            }
            else{
                if(len==0){
                    arr[i]=0;
                    i++;
                }
                else{
                    len=arr[len-1];
                }
            }
        }
        return arr;
    }

    static int stringSearch(String haystack, String needle){
        int lenStr=haystack.length(), lenPat=needle.length();
        int[] prefixArray = computeLps(needle);
        int i=0,j=0, index=-1;
        while( i<lenStr ){
            if( haystack.charAt(i)==needle.charAt(j) ){
                i++;
                j++;
            }

            if( j==lenPat ){
                index = i-j;
                return index;
            }
            else if( i<lenStr && haystack.charAt(i)!=needle.charAt(j) ){
                if( j==0 ){
                    i++;
                }
                else{
                    j=prefixArray[j-1];
                }
            }
        }

        return index;
    }
    public static void main(String[] args){
        //int[] arr=computeLps("aaacaaaaac");
        String haystack="aabacaaabaaa", needle="aabaa";
        System.out.println(stringSearch(haystack, needle)); 
    }
}
