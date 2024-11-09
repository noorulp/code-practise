
//LeetCode 209

class MinSizeSubArray{

    static int minSubArrayLen(int target, int[] nums){
        //build prefixArray
        int length=nums.length;
        int minLength = -1;
        int[] prefixArray = new int[nums.length];
        prefixArray[0]=nums[0];
        for(int i=1;i<length; i++){
            prefixArray[i] = prefixArray[i-1] + nums[i];
            if( nums[i]>=target ) //handle for set size 1
                return 1;
        }
        //handle for not found
        if( prefixArray[length-1] < target)
            return 0;
        
        //find sums using binary search on prefix array
        for(int i=0; i<length-1; i++){

            int newTarget;
            if( i==0 ){
                newTarget = target;
            } 
            else{
                newTarget = target + prefixArray[i-1];
            }
            //binary search
            int low=i, high=length-1; 
            while( low <= high ){
                int mid = low + ( high - low)/2;
                if( prefixArray[mid] > newTarget ){
                    high= mid - 1;
                }
                else if( prefixArray[mid] < newTarget ){
                    low = mid + 1;
                }
                else{
                    low=mid;
                    break;
                }    
            }
            
            int size = low - i + 1;
            if( low < length && prefixArray[low] >= newTarget && (size < minLength || minLength == -1) ){
                minLength = size;
            }

        }

        return minLength;
    }

    public static void main(String[] args){
        int[] nums= { 1,2,3,4,5 };
        int target = 11;
        System.out.println(minSubArrayLen(target, nums)); 
    }
}