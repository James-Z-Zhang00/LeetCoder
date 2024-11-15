# 12. Integer to Roman

# 46ms 16.26MB
# 86.73% 81.99%

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''

        numeric_dic = {
            1:'I',
            10:'X',
            100:'C',
            1000:'M',

            4:'IV',
            5: 'V',
            9:'IX',
            40:'XL',
            50: 'L',
            90:'XC',
            400:'CD',
            500: 'D',
            900:'CM'
        }

        for n in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
            while n <= num:
                result += numeric_dic[n]
                num -= n
        return result

solution = Solution()
print('3:', solution.intToRoman(3))
print('58:', solution.intToRoman(58))
print('1994:', solution.intToRoman(1994))

