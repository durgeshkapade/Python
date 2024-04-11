def factorial(nums):
    
    if(nums<=1):
        return nums
    
    
    ans=nums*factorial(nums-1)
    return ans
  
  
nums=9
  
p=factorial(nums)
print(p)