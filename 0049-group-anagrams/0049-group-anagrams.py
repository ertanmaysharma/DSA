class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        for word in strs :
            sorted_words = ''.join(sorted(word))
            anagram_map[sorted_words].append(word)
        return list(anagram_map.values())     