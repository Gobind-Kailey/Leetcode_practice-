class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = 1
        holder = 1
        while holder <= (len(nums) - 1):
            if nums[i] + nums[j] == target:
                return [i, j]
            elif j == (len(nums) - 1):
                i += 1
                holder += 1
                j = holder
            else:
                j += 1

        # Wrong 
        # num_sort = nums.sort()
        # num_sort = nums # This line is redundant since nums is already sorted in place
        # array_len = len(nums); 

        # i = 0   
        # j = array_len - 1
        # # print("Anny")
        # if array_len %2 == 0:
        #     while i != j:  # // # i think this already takes care of the minus 1
        #         if num_sort[i] + num_sort[j] == target: 
        #             print(num_sort[i], num_sort[j])
        #             return [i, j]

        #         if num_sort[i] + num_sort[j] > target:
        #             j -=1

        #         if num_sort[i] + num_sort[j] < target:
        #             i +=1
        # else:
        #     while((i+1)!=j):
        #         if num_sort[i] + num_sort[j] == target:
        #             print(num_sort[i], num_sort[j])
        #             print("indexs", i, j)
        #             return [i, j]

        #         if num_sort[i] + num_sort[j] > target:
        #             j -=1

        #         if num_sort[i] + num_sort[j] < target:
        #             i +=1


    

twosum_1 = Solution() # Create an instance of the Solution class
print(twosum_1.twoSum([3,2,4], 6)) # Call the twoSum method and print the result


            

        
        



        