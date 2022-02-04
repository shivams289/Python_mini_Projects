class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
      
        for el in operations:
            if el[0] == '-' or el[-1] == '-':
                ans = ans -1
            else:
                ans = ans+1
        return ans