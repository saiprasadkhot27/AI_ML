
class Solution:
    def countAndSay(self, n: int) -> str:

        s = "1"

        for i in range(n - 1):
            result = ""
            j = 0

            while j < len(s):
                count = 1

                while j + 1 < len(s) and s[j] == s[j + 1]:
                    count += 1
                    j += 1

                result += str(count) + s[j]
                j += 1

            s = result

        return s
