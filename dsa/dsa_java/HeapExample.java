package dsa_java;

class MaxHeap{
    
    int maxSize;
    int[] arr;
    int heapSize;

    MaxHeap(int size){
        this.maxSize = size;
        this.arr = new int[this.maxSize];
        this.heapSize = 0;
    }

    int parent(int i){
        //return index of parent of ith node
        return (i-1)/2; 
    }

    int lchild(int i){
        //return left child node index of ith node
        return 2 * i + 1;
    }

    int rchild(int i){
        //return right child node index of ith node
        return 2 * i + 2;
    }

    void maxHeapify(int i){
        //takes inedx i and heapifies the tree
        int l = this.lchild(i);
        int r = this.rchild(i);
        int largest = i;
        
        if( l < this.heapSize && arr[largest] < arr[l] ){
            largest = l;
        }
        if( r < this.heapSize && arr[largest] < arr[r] ){
            largest = r;
        }

        if( largest!= i){
            //swap i and largest
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;

            maxHeapify(largest);
        }

    }

}

public class HeapExample {
    public static void main(String[] args){
        
    }
}
