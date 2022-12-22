"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k."""

nums = [1,2,3,1]
k = 3
def containsNearbyDuplicate(list,k):
       
        numHash = {} 
        for i,j in enumerate(list):
            if j in numHash and i - numHash[j] <=k: 
                return True
            numHash[j]=i
        return False 

sol = containsNearbyDuplicate(nums,k)
print(sol)