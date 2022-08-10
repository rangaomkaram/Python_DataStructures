from rough import binary_search
def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return print('left')
            return print('found')

        elif nums[mid] < target:
            return print('right')

        else:
            return print('left')
    
    return binary_search(0,len(nums)-1, condition)

def last_position(nums,target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return print('right')
            return print('found')
        elif nums[mid] < target:
            return print('right')
        else:
            return print('left')
    return binary_search(0,len(nums)-1, condition)


def first_and_last_position(nums,target):
    return print(first_position(nums,target) , last_position(nums,target))


nums = [5,7,7,8,8,10]
target = 5

first_and_last_position(nums=nums,target=target)







