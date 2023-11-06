# _*_ coding:UTF-8 _*_
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
            print(lookup)
        return max_len

if __name__ == '__main__':
    A=Solution()
    s = "abcabcbb"
    print(A.lengthOfLongestSubstring(s))