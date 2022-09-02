class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            int_string = str(x)
            length = len(int_string)
            for i in range(length):
                if int_string[i] == int_string[length - 1]:
                    length = length - 1
                    continue
                else:
                    return False
            return True