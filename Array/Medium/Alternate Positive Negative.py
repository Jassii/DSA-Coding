#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        neg = []
        pos = []
        for i in range(0,len(arr)):
            if(arr[i]>=0):
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        
        #now i have both positive and negative integer arrays.
        
        result=[]
        p=len(pos)
        n=len(neg)
        
        i=0 #index for positive array
        j=0 #index for negative array
        
        k=0 #just to decide which element should be picked
        
        while(i<p and j<n):
            if(k%2==0): #for positive
                result.append(pos[i])
                i+=1
            else: #for negative
                result.append(neg[j])
                j+=1
            k+=1
        
        #for the remaining element in any one of the array (pos and neg)
        while(i<p):
            result.append(pos[i])
            i+=1
        while(j<n):
            result.append(neg[j])
            j+=1

      #place element present in result in the arr array
        for i in range(0,len(result)):
            arr[i]=result[i]
        
        return arr
