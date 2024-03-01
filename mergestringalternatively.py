class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        # convert word1 n word2 in list as string can't be upadted in python
        word1 = list(word1)
        word2 = list(word2)
        # the pointer is at 0
        i = 0
        # create an empty list to store the merge list

        merged = []

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])

        return ''.join(merged)

