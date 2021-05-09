class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0]*(len(num1) + len(num2))
        for i,x in enumerate(reversed(num1)):
            for j,y in enumerate(reversed(num2)):
                a = int(x)*int(y) + result[i+j]
                result[i+j] = int(a%10)
                result[i+j+1] = result[i+j+1] + int(a/10)
        last = 0
        for i in range(len(result)-1, -1, -1):
            if result[i] != 0:
                last = i
                break
        answer = "".join(map(str, reversed(result[0:last+1])))
        return answer
