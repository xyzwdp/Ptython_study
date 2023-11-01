class Solution():
    def twosum(self,nums,target):
        for i in range(len(nums)):
            # print(i)
            for j in range(i+1,len(nums)):
                # print(j)
                sum=nums[i]+nums[j]
                if sum==target:
                    return [i,j]


if __name__ == '__main__':
    nums=[15,2,11,7]
    target=9
    SUM=Solution()
    print(SUM.twosum(nums,target))