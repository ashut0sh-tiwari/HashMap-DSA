"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

nums = [1,2,3,1]

def containsDuplicate(list): 
        numHash = {} #initialising the variable
        for i,j in enumerate(list): #iterating using enumerate function
            if j not in numHash: #if element not in dict then push that character in dict with i index
                numHash[j]=i
            else: #else return true
                return True
        return False #return false if duplicate not find

solution = containsDuplicate(nums)
print(solution)