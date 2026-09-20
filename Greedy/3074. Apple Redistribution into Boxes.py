class Solution(object):
    def minimumBoxes(self, apple, capacity):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        total=sum(apple)
        capacity.sort(reverse=True)
        box=0
        for i in capacity:
            total-=i
            box+=1
            if total<=0:
                break
        return box