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