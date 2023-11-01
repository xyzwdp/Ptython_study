"""
时间复杂度：O(N)
空间复杂度：0(N)
以空间换时间，这样运行效率更高
"""
class Solution:
    def twosum(self, nums, targete):
        # 创建一个空字典
        hasetable = {}
        # 实现对nums的这个列表进行一个排序
        for i, num in enumerate(nums):
            print(i)
            if targete - num in hasetable:
                print(targete - num)
                #此处涉及列表的访问知识
                return [hasetable[targete - num],i]
            # 设计的知识，字典key-value键值对添加知识
            hasetable[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 3, 7, 4]
    target = 6
    SUM = Solution()
    print(SUM.twosum(nums, target))
