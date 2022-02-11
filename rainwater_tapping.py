def trap(self, height: List[int]) -> int:
    n = len(height)
    left = []
    right = [0]*n
    val = height[0]
    val1 = height[-1]
    for i in range(n):
        left.append(max(height[i], val))
        val = max(height[i], val)
        right[n-i-1] = (max(height[n-i-1], val1))
        val1 = max(height[n-i-1], val1)
        
   
    ans = 0 
    for i in range(n):
        ans += (min(left[i], right[i]) - height[i])
        
    return ans