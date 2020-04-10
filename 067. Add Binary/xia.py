class Solution:
    def addChar(self, a, b, token = '0'):
        _sum = a + b + token
        if _sum == '111':
            return '11'
        elif _sum == '101' or _sum == '011' or _sum == '110':
            return '10'
        elif _sum == '000':
            return '00'
        elif _sum == '010' or _sum == '100' or _sum == '001':
            return '01'

    def charGen(self, string):
        i = len(string) - 1
        while i >= 0:
            yield string[i]
            i -= 1
        return None

    def none2zero(self, char):
        return '0' if char == None else char

    def addBinary(self, a: str, b: str) -> str:
        aGen = self.charGen(a)
        bGen = self.charGen(b)

        sum_res = ''

        _temp_token = '0' # 进位信息

        while True:
            try:
                nextA = next(aGen)
            except StopIteration as e:
                nextA = e.value

            try:
                nextB = next(bGen)
            except StopIteration as e:
                nextB = e.value


            if nextA == None and nextB == None:
                break

            nextA = self.none2zero( nextA )
            nextB = self.none2zero( nextB )

            _sum = self.addChar(nextA, nextB, _temp_token)

            print(nextA, nextB, _sum)

            sum_res += _sum[1]
            _temp_token = _sum[0]

        sum_res += '' if _temp_token == '0' else '1'
        return sum_res[::-1]

# test code 
s = Solution()
print(s.addBinary('100', '1111'))