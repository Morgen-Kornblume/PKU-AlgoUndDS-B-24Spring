class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #字母异位词分组，分别统计每个字符串中字母出现的次数，然后用一个元组表示，最后用哈希表存储
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())