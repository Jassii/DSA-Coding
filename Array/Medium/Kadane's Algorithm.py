import sys
class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        
        # kadane's algorithm - Optimized Approach
        currSum=0  #current sum
        maxSum=-sys.maxsize-1.  #smallest value of integer
        for i in range(0,len(arr)):
            currSum = max(arr[i],currSum+arr[i])
            maxSum = max(maxSum,currSum)
        
        return maxSum
        
        #brute force approach, taking out all subarrays and taking out its sum
        # maxSum = -sys.maxsize-1
        # for i in range(0,len(arr)):
        #     for j in range(i,len(arr)):
        #         total=0
        #         for k in range(i,j+1):
        #             total += arr[k]
        #         maxSum=max(maxSum,total)
        # return maxSum
