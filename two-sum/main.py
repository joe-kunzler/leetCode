nums =[2,7,11,15]
target = int

def twoSum(nums, target):
    print(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                if i != j:
                    return [i, j]
                else:
                    continue