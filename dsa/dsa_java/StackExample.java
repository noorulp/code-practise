package dsa_java;

class Stack{

    int maxSize;
    int[] stack;
    int index;

    public Stack(int n){
        this.maxSize = n;
        this.stack = new int[n];
        this.index = 0;
    }

    public boolean push(int ele){
        if( this.isFull() ){
            return false;
        }
        this.index++;
        this.stack[index] = ele;
        return true;
    }

    public int pop(){
        if( this.isEmpty() )
            return Integer.MIN_VALUE;
        
        return this.stack[this.index--];
    }

    public int peek(){
        if( this.isEmpty() )
            return Integer.MIN_VALUE;

        return this.stack[this.index];
        
    }

    public boolean isEmpty(){
        return this.index == -1;
    }

    public boolean isFull(){
        return this.index == this.maxSize;
    }

}

public class StackExample {
    
    public static void main(String[] args){

        Stack s = new Stack(20);
        s.push(10);
        s.push(15);
        s.push(80);
        System.out.println(s.pop());
        System.out.println(s.peek());
        System.out.println(s.pop());

    }
}
