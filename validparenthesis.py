class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # first make a dict with pairs
        bracket_pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        # Now make a stack, where you can store the values
        stack = []
        # now c is on the oth index pointing the first bracket
        for c in s:
            # check for open bracket
            if c in bracket_pairs:
                stack.append(c)  # add the open brackets
            elif len(stack) == 0 or c != bracket_pairs[
                stack.pop()]:  # if stack is empty and brackets pairs is not equal to
                return False
        # if stack is empty
        return len(stack) == 0
