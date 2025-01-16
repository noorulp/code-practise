import heapq

if __name__ == '__main__':
    li = [1, 3, 5, 7, 9]
    # using heapify to convert list into heap
    heapq.heapify(li)
    # printing created heap
    print ("The created heap is : ", (list(li)))

    while li:
        print(heapq.heappop(li))
    