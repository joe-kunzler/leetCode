class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == '':
            return 0
        else:
            if s[0] == '-' or s[0] == '+':
                if s[0] == '-':
                    sign = -1
                else:
                    sign = 1
                s = s[1:]
            else:
                sign = 1
            if s == '':
                return 0
            else:
                if s[0].isdigit():
                    for i in range(len(s)):
                        if s[i].isdigit():
                            continue
                        else:
                            s = s[:i]
                            break
                    if sign == -1:
                        if int(s) >= 2147483648:
                            return -2147483648
                        else:
                            return -int(s)
                    else:
                        if int(s) >= 2147483647:
                            return 2147483647
                        else:
                            return int(s)
                else:
                    return 0