class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                total = mul + res[i+j+1]

                res[i+j+1] = total % 10
                res[i+j] += total // 10

        return ''.join(map(str, res)).lstrip('0')