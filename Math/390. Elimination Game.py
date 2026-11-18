class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod=1337
        p=''
        for i in b:
            p+=str(i)
        p=int(p)

        return pow(a,p,mod)