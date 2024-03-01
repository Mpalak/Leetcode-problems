class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
      """
        # Find out the greatest number of candies among all kids
        maxCandies = max(candies)
        # now check for each kid , if they will have greatest no of candies
        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCandies)

        return result