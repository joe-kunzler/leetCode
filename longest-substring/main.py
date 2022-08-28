class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        max_len = 1
        start = 0
        end = 1
        while end < len(s):
            if s[end] in s[start:end]:
                start = s[start:end].index(s[end]) + 1 + start
                print(start)
            else:
                end += 1
                max_len = max(max_len, end - start)
                print("max_len: ", max_len)
        return max_len