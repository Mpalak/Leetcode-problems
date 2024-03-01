class Solution(object):
    def gcdOfStrings(self, str1, str2):
        #if s1 n s2 is not equal and there is no common divisor possible,return empty string
        if str1 + str2 != str2 + str1:
            return ""
#if length of both str r equal,then we return either s1 or s2
        if len(str1) == len(str2):
            return str1
#if s1 is greater than s2,then we remove the matching string and we get the divisor
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
   # if s2 is greater than s1, then we recurse withe the substring of s2,after removing the prefix that matches s1
        return self.gcdOfStrings(str1, str2[len(str1):])