class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])+1):
            max_prefix = strs[0][:-i]
            if all(max_prefix in s for s in strs):
                return max_prefix
            else:
                return ''    