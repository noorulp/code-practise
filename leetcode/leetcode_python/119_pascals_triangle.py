
class Solution:
    
    def getRow(self, rowIndex: int) -> list[int]:
        row = []
        
        for i in range(0, rowIndex + 1, 1):
            row.append(1)
            j = i - 1
            while j > 0:
                row[j] = row[j-1] + row[j]   

        return row        


if __name__ == "__main__":
    '''
    '''
    sol = Solution()
    print(sol.getRow(1))
