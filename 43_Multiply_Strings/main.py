class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self._getNumber(num1) * self._getNumber(num2))

    def _getNumber(self, digits: str):
        num = 0
        for digit in digits:
            num = num * 10 + int(digit)
        return num