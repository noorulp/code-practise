class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prods = []

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
            self.prods = [] # product becomes zero so reset
            return
        n = len(self.nums)
        self.nums.append(num)
        if n == 0:
            self.prods.append(num)
        else:
            self.prods.append(num * self.prods[-1])

    def getProduct(self, k: int) -> int:
        n = len(self.nums)
        if k > n: # zero reset the product so return 0
            return 0
        if k == n:
            return self.prods[-1]
        return self.prods[n - 1] // self.prods[n - k -1]
        

def test(input1: list, input2: list):
    i = 1
    n = len(input2)
    sol = ProductOfNumbers()
    while i < n:
        if input1[i] == "add":
            sol.add(input2[i][0])
            print(sol.nums)
        else:
            prod = sol.getProduct(input2[i][0])
            print("product" + str(input2[i][0]) + str(prod))
        i += 1

if __name__ == '__main__':
    test(["ProductOfNumbers","add","get","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"], 
         [[],[3], [1], [0],[2],[5],[4],[2],[3],[4],[8],[2]])
    