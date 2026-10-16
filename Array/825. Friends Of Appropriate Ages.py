class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0] * 121
        for age in ages:
            count[age] += 1
        res = 0
        for age in range(15, 121):
            for other in range(age // 2 + 8, age + 1):
                res += count[age] * count[other]

                if age == other:
                    res -= count[age]
        return res